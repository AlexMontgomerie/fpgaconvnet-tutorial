import numpy as np
import tutorial_library

from matplotlib import pyplot as plt
import sys


def main():

    #Simple command line parsing
    fpga_serial = sys.argv[1]

    #Optional third argument
    if len(sys.argv) == 2:
        mnist_idx = 0
    elif len(sys.argv) > 2:
        mnist_idx = int(sys.argv[2])

    print(f"The index is: {mnist_idx}")

    # Grab image from dataset
    mnist_image = tutorial_library.get_MNIST_image(mnist_idx)

    #Optional input featuremap display
    # print(tutorial_library.get_MNIST_label(mnist_idx))
    # Display image
    # plt.imshow(mnist_image[0][0], interpolation='nearest')
    # plt.show()

    print("Beginning featuremap upload")
    # FPGA upload
    tutorial_library.send_array(fpga_serial, mnist_image[0][0])

    # Confirm featuremap reception / additional status messages
    print(tutorial_library.receive_string(fpga_serial))
    print(tutorial_library.receive_string(fpga_serial))
    # Additional debug status message to print out the output values (without divided by 256)
    # print(tutorial_library.receive_string(fpga_serial))
    flat_fpgaoutput = tutorial_library.receive_array(fpga_serial)
    print(tutorial_library.receive_string(fpga_serial))

    # Reference ONNX computations
    output = tutorial_library.run_inference("models/single_layer.onnx", mnist_image)
    output = output[0][0]

    #Flattening for array preview
    fpgaoutput = np.reshape(flat_fpgaoutput, (24, 24, 16))
    flat_output = output.flatten()

    #Array comparison print
    print(f"Flat FPGA readout ({fpgaoutput.size} items):")
    print(flat_fpgaoutput)
    print(f"Flat Reference readout ({output.size} items):")
    print(flat_output)

    # reshape to enable comparison 
    fpgaoutput_reshaped = np.transpose(fpgaoutput, (2, 0, 1))
    #Error information
    err = (np.square(fpgaoutput_reshaped - output)).mean(axis=None)
    print(f"The mean squared error was: {err}")
    return


if __name__ == '__main__':
    main()
