import numpy as np
import onnxruntime
import serial


# Grabs image at index idx from the MNIST testing dataset
def get_MNIST_image(idx):
    # Read the mnist binary format
    image_path = "MNIST/t10k-images-idx3-ubyte"
    with open(image_path, 'rb') as fh:
        fh.seek(16 + idx * (28 * 28), 0)
        arr = list(fh.read(28 * 28))
    arr = np.array(arr)
    arr = arr.astype('float32')

    # Normalize array [-1, 1]
    arr = np.subtract(arr, (np.amax(arr) + np.amin(arr)) / 2)
    arr = np.multiply(arr, 1 / np.amax(arr))

    arr = np.reshape(arr, (28, 28))
    arr.transpose()

    # Batches for onnx run
    arr = np.reshape(arr, (1, 1, 28, 28))
    # arr = np.tile(arr, (42, 1, 1, 1))
    return arr


# Grabs corresponding label at index idx from the MNIST testing dataset
def get_MNIST_label(idx):
    label_path = "MNIST/t10k-labels-idx1-ubyte"
    with open(label_path, 'rb') as fh:
        fh.seek(8 + idx, 0)
        return int(fh.read(1)[0])

# Runs inference using the onnxruntime
def run_inference(model_path, input):
    ort_sess = onnxruntime.InferenceSession(model_path)
    return ort_sess.run(["4"], {"input.1": input})

# Sends 8 bit grayscale image to FPGA
def send_array(serial_descriptor, arr):
    # convert to 16 bit (8 fractional bit) fixed point format
    arr = np.multiply(arr, 256)
    arr = arr.astype('int32')

    # Serialize to space delimited ascii string
    arr = arr.flatten('C')
    arrstr = ""

    for pixel in arr:
        arrstr += str(pixel) + " "

    # End string in newline
    arrstr = (arrstr[:-1] + '\n').encode('ascii', 'replace')

    # Send over serial
    with serial.Serial(port=serial_descriptor, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None,
                       xonxoff=0,
                       rtscts=0) as ser:
        ser.write(arrstr)
    return

#Decodes received string from FPGA as array
def receive_array(serial_descriptor):
    with serial.Serial(port=serial_descriptor, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None,
                       xonxoff=0,
                       rtscts=0) as ser:
        line = ser.readline()

    flat_fpgaoutput = list(map(int, line.split()))
    flat_fpgaoutput = np.array(flat_fpgaoutput).astype('float32')
    flat_fpgaoutput = np.divide(flat_fpgaoutput, 256)
    return flat_fpgaoutput

#Returns line received from FPGA
def receive_string(serial_descriptor):
    with serial.Serial(port=serial_descriptor, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None,
                       xonxoff=0, rtscts=0) as ser:
        return ser.readline().decode('ascii')
