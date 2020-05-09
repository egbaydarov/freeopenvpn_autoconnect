# freeopenvpn_autoconnection 
* [download](https://github.com/egbaydarov/freeopenvpn_autoconnect/releases/download/WORKING/VPN.zip)

# NOTE: administrator rights and openvpn istalled in PATH variables are required

-------------
## Python packages and setup guides

* `pip install tensorflow==2.0.0`

* [models v1.13](https://github.com/tensorflow/models/archive/v1.13.0.zip)

* [Protobuff](https://github.com/protocolbuffers/protobuf/releases/download/v3.11.4/protoc-3.11.4-win64.zip)

* [Protobuf compilation guide](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html)

* compile batch comand `for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.`

* `pip install opencv-python`
 
* OpenVpn PATH example `setx path %path%;"c:\Program Files\OpenVPN\bin"`
