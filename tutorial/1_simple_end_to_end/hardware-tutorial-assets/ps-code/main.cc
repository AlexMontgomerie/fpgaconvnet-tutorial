#include "xfpgaconvnet_ip.h"
#include "xil_io.h"
#include "xil_cache.h"
#include "sleep.h"
#include "xtime_l.h"

#include <iostream>
#include <string>

#define COARSE_IN 1
#define COARSE_OUT 4

#define INPUT_SHAPE 1*28*28
#define OUTPUT_SHAPE 24*24*16
#define fixed_t u16

#define FPGACONVNET_PL_RUN_PARTITIONS 	0

#define RUNS 65536


int main(){
	//Allocate memory areas
	volatile u64* input = new u64[INPUT_SHAPE/COARSE_IN];
	volatile u64* output = new u64[OUTPUT_SHAPE/COARSE_OUT];
	XFpgaconvnet_ip hw;

	//Initialize IP
	XFpgaconvnet_ip_Initialize(&hw, XPAR_FPGACONVNET_IP_0_DEVICE_ID);

    std::string in;

    while(1){

		//Parse and load input featuremap from UART
		for (int i = 0; i< INPUT_SHAPE; i++){
			std::cin >> in;
			input[i] = ((u64) std::stoi(in)) & 0x000000000000ffff;
		}

		usleep(100000);

		//Flush cache
	    Xil_DCacheFlush();
		std::cout<<  "Featuremap upload complete \n";

		// IP control setup
		XFpgaconvnet_ip_Set_mode(&hw,FPGACONVNET_PL_RUN_PARTITIONS);

		XTime t_start, t_end;
		XTime_GetTime(&t_start);

		//Set input and output addresses
		XFpgaconvnet_ip_Set_fpgaconvnet_in_0( &hw, (u32) input);
		XFpgaconvnet_ip_Set_fpgaconvnet_out_0(&hw, (u32) output);

		//1024 runs for better time estimation
		for(int i = 0; i<RUNS; i++){

			XFpgaconvnet_ip_Start(&hw);

			//Wait for IP to finish
			while(!XFpgaconvnet_ip_IsReady(&hw));
		}

		XTime_GetTime(&t_end);
		std::cout << "Beginning download \n";
		usleep(100000);

		//Invalidate cache
		Xil_DCacheInvalidate();

		//Dump output
		for(int i = 0; i<OUTPUT_SHAPE; i++){
			// load address, the processor is byte addressable, hence each address is 8 bits
			std::cout << Xil_In16(((u64) output) + 2*i) << " ";
			usleep(50);
		}
		std::cout << '\n';

		usleep(100000);
		float t_run = (t_end - t_start)* 1000000. /COUNTS_PER_SECOND;
		std::cout<< "Completed " << RUNS << " Runs.  Time taken (us): " << (int) t_run << "  Rate (img/s): " << 1/t_run * RUNS * 1000000 << "\n";
	    Xil_DCacheFlush();
    }

    return 0;
}
