<!DOCTYPE html>
<html>
<head>
</head>
<body>

<p align="center">
  <img src="noisebuster.png" alt="NoiseBuster Logo">
</p>

<p>
NoiseBuster is an advanced Python application designed to monitor and log noise levels using a USB-connected sound meter. It not only records noise events but also integrates with various services like InfluxDB, MQTT, Discord, and more to provide a comprehensive noise monitoring solution. With features like weather data integration and traffic data collection, NoiseBuster offers a versatile tool for environmental monitoring and analysis.
</p>

<p align="center">
  <img src="noisebuster_grafana.png" alt="NoiseBuster Dashboard">
  <br>
  <em>NoiseBuster Dashboard in Grafana showing noise events over time.</em>
</p>
<p align="center">
  <img src="noisebuster_home_assistant.png" alt="NoiseBuster Analytics">
  <br>
  <em>Detailed analysis of noise levels correlated with traffic data.</em>
</p>

<hr>

<h2>Discord Server</h2>

<p>
Join the community on our Discord server to discuss, contribute, and get support: <a href="https://discord.gg/pCxtsg7mBN">NoiseBuster Discord Server</a>
</p>

<h2>Features</h2>

<ul>
    <li><strong>Noise Monitoring:</strong> Interfaces with a USB sound meter to monitor and record noise levels in real-time.</li>
    <li><strong>Data Storage:</strong> Stores recorded noise events in InfluxDB for easy retrieval and analysis.</li>
    <li><strong>MQTT Integration (<em>Optional</em>):</strong> Publishes noise levels and events to an MQTT broker for integration with home automation systems like Home Assistant.</li>
    <li><strong>Weather Data Collection (<em>Optional</em>):</strong> Fetches current weather data from OpenWeatherMap API to correlate noise events with weather conditions.</li>
    <li><strong>Traffic Data Collection (<em>Optional</em>):</strong> Integrates with Telraam API to collect traffic data, allowing analysis of noise levels in relation to traffic conditions. <em>Note: A dedicated YOLO-powered traffic counting script is in development and will be available soon.</em></li>
    <li><strong>Image Capture (<em>Optional</em>):</strong> Captures images using an IP camera or Raspberry Pi camera when noise levels exceed a specified threshold.</li>
    <li><strong>Notifications (<em>Optional</em>):</strong> Sends notifications via Discord and Pushover when certain events occur (e.g., high noise levels, API failures).</li>
    <li><strong>Configurable Timezone:</strong> Adjusts timestamps according to the specified timezone offset.</li>
    <li><strong>Error Handling and Logging:</strong> Robust error handling with detailed logging for troubleshooting.</li>
</ul>

<h2>Usages</h2>

<ul>
    <li>Monitor loud traffic, planes, live events, and more.</li>
    <li>Create insightful graphics to share statistics with authorities.</li>
    <li>Analyze environmental noise in correlation with weather and traffic data.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<p>Before using NoiseBuster, ensure the following prerequisites are met:</p>

<ul>
    <li>Linux-based system (e.g., Ubuntu, Debian, Raspberry Pi OS).</li>
    <li>Python 3.6 or higher installed.</li>
    <li>A USB-connected sound level meter. All models with USB communication capabilities should work. Other types like RS485 models and ESP devices with calibrated microphones could be used, but may require additional setup by the user.</li>
    <li>Internet connection for API integrations (e.g., OpenWeatherMap, Telraam).</li>
    <li><strong>Optional but recommended:</strong> InfluxDB 2.x and Grafana for data storage and visualization.</li>
    <li><strong>Optional:</strong> MQTT broker if you wish to publish data to an MQTT broker.</li>
    <li><strong>Optional:</strong> Docker installed for containerized deployment.</li>
</ul>

<h3>Installation</h3>

<ol>
    <li>Clone the NoiseBuster repository from GitHub:

    <pre>git clone https://github.com/silkyclouds/NoiseBuster.git</pre>
    </li>
    <li>Navigate to the directory:

    <pre>cd NoiseBuster</pre>
    </li>
    <li>Create a virtual environment (recommended):

    <pre>
python3 -m venv env
source env/bin/activate
    </pre>
    </li>
    <li>Install the requirements:

    <pre>pip install --upgrade pip
pip install -r requirements.txt</pre>
    </li>
</ol>

<h3>Hardware Requirements</h3>

<ul>
    <li><strong>USB Sound Meter:</strong>
        <ul>
            <li>The application is designed to work with USB-connected sound level meters.</li>
            <li><strong>Example Device:</strong> <a href="https://www.aliexpress.com/item/32995118902.html">USB Sound Level Meter on AliExpress</a></li>
            <li>Ensure the device supports USB communication.</li>
            <li>For devices not automatically detected, you may need to specify the USB vendor ID and product ID in the configuration. Use the <code>lsusb</code> command to find these IDs.</li>
        </ul>
    </li>
    <li><strong>Camera (<em>Optional</em>):</strong>
        <ul>
            <li><strong>IP Camera:</strong> Supports RTSP or HTTP protocols. Provide the camera's URL in the configuration.</li>
            <li><strong>Raspberry Pi Camera:</strong> Connects directly to the Raspberry Pi. Requires the <code>picamera</code> library.</li>
        </ul>
    </li>
</ul>

<h2>Configuration</h2>

<p>All configuration settings are stored in the <code>config.json</code> file. Here is how to set up your configuration:</p>

<ol>
    <li>Open <code>config.json</code> in a text editor. Keep all default IP addresses as <code>localhost</code> or <code>127.0.0.1</code> to ensure it works out of the box.</li>
    <li>Configure each section:

        <ul>
            <li><strong>InfluxDB Configuration:</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to store data in InfluxDB.</li>
                    <li>Provide your InfluxDB <code>host</code>, <code>port</code>, <code>token</code>, <code>org</code>, and bucket names.</li>
                    <li>Ensure you create buckets named exactly as in the config sample (<code>"noise_buster"</code> and <code>"noise_buster_realtime"</code>) unless you know what you're doing.</li>
                    <li><strong>Important:</strong> If you're new to InfluxDB, follow the official <a href="https://docs.influxdata.com/influxdb/v2.0/get-started/">InfluxDB setup guide</a> to create your organization, buckets, and API tokens.</li>
                </ul>
            </li>
            <li><strong>Pushover Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to receive Pushover notifications.</li>
                    <li>Provide your <code>user_key</code> and <code>api_token</code>. Sign up at <a href="https://pushover.net/">Pushover</a>.</li>
                </ul>
            </li>
            <li><strong>Weather Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to fetch weather data.</li>
                    <li>Provide your OpenWeatherMap <code>api_key</code> and <code>location</code>. Sign up at <a href="https://openweathermap.org/api">OpenWeatherMap API</a>.</li>
                </ul>
            </li>
            <li><strong>MQTT Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to publish data to an MQTT broker.</li>
                    <li>Provide your MQTT <code>server</code>, <code>port</code>, <code>user</code>, and <code>password</code>. Learn more about MQTT at <a href="https://mqtt.org/">mqtt.org</a>.</li>
                </ul>
            </li>
            <li><strong>Camera Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"use_ip_camera": true</code> or <code>"use_pi_camera": true</code> depending on your setup.</li>
                    <li>Provide the <code>ip_camera_url</code> if using an IP camera.</li>
                </ul>
            </li>
            <li><strong>Device and Noise Monitoring Configuration:</strong>
                <ul>
                    <li>Set <code>device_name</code> for identification.</li>
                    <li>Set <code>minimum_noise_level</code> in decibels to trigger events.</li>
                    <li>Specify <code>image_save_path</code> where images will be stored.</li>
                    <li>Provide <code>usb_vendor_id</code> and <code>usb_product_id</code> if automatic USB device detection fails. Use <code>lsusb</code> to find these IDs.</li>
                </ul>
            </li>
            <li><strong>Telraam API Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to collect traffic data.</li>
                    <li>Provide your Telraam <code>api_key</code> and <code>segment_id</code>. Learn more at <a href="https://telraam.net/">Telraam</a>.</li>
                    <li><em>Note:</em> A dedicated YOLO-powered traffic counting script is in development and will be available soon.</li>
                </ul>
            </li>
            <li><strong>Timezone Configuration:</strong>
                <ul>
                    <li>Set <code>timezone_offset</code> relative to UTC.</li>
                </ul>
            </li>
            <li><strong>Discord Configuration (<em>Optional</em>):</strong>
                <ul>
                    <li>Set <code>"enabled": true</code> to send notifications to Discord.</li>
                    <li>Provide your Discord <code>webhook_url</code>. Create one at <a href="https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks">Discord Webhooks</a>.</li>
                </ul>
            </li>
        </ul>
    </li>
    <li>Save <code>config.json</code>.</li>
</ol>

<h2>Running the Script</h2>

<h3>Using Docker (Recommended)</h3>

<p>The easiest way to get started is by using Docker. A <code>docker-compose.yml</code> file is provided to set up all the necessary components.</p>

<ol>
    <li>Ensure Docker and Docker Compose are installed on your system. Learn more at <a href="https://docs.docker.com/get-docker/">Docker Installation</a>.</li>
    <li>Navigate to the project directory:

    <pre>cd NoiseBuster</pre>
    </li>
    <li>Edit the <code>docker-compose.yml</code> file if necessary.</li>
    <li>Run Docker Compose:

    <pre>docker-compose up -d</pre>
    </li>
    <li>Pass the USB device to the Docker container:
        <ol>
            <li>List your USB devices using the <code>lsusb</code> command.</li>
            <li>Identify your USB sound meter in the list.</li>
            <li>Note the Bus and Device IDs (e.g., Bus 003 Device 011).</li>
            <li>Modify the <code>devices</code> section in <code>docker-compose.yml</code> to include your device:

            <pre>
devices:
  - "/dev/bus/usb/003/011:/dev/bus/usb/003/011"
            </pre>
            </li>
        </ol>
    </li>
    <li>Check the logs to ensure it's running correctly:

    <pre>docker-compose logs -f</pre>
    </li>
</ol>

<h3>Using Python Directly</h3>

<ol>
    <li>Ensure the USB sound meter is connected to your computer.</li>
    <li>Activate the virtual environment if you created one:

    <pre>source env/bin/activate</pre>
    </li>
    <li>Run the application:

    <pre>python noisebuster.py</pre>
    </li>
</ol>

<h2>Tips and Tricks</h2>

<ul>
    <li><strong>Testing Noise Events:</strong> To test the setup, generate a loud noise near the sound meter. Check the logs or your InfluxDB to see if the event was recorded.</li>
    <li><strong>Virtual Environment Issues:</strong> If you encounter issues running the script, ensure you are in the virtual environment. Activate it using <code>source env/bin/activate</code>.</li>
    <li><strong>Device Detection:</strong> If the USB sound meter is not detected, specify <code>usb_vendor_id</code> and <code>usb_product_id</code> in <code>config.json</code>. Use the <code>lsusb</code> command to find these IDs.</li>
    <li><strong>Feature Enabling/Disabling:</strong> Many features like Pushover notifications, weather data, MQTT, and Telraam integration are optional. Enable or disable them in the <code>config.json</code> file as needed.</li>
    <li><strong>Using Other Hardware:</strong> While the application is designed for USB sound meters, other types like RS485 models and ESP devices with calibrated microphones could be used but may require additional setup and modifications to the code.</li>
</ul>

<h2>InfluxDB and Grafana Setup</h2>

<p>To visualize and analyze the data collected by NoiseBuster, set up InfluxDB and Grafana.</p>

<h3>InfluxDB Setup</h3>

<ol>
    <li>Install InfluxDB. Follow the official <a href="https://docs.influxdata.com/influxdb/v2.0/get-started/">InfluxDB installation guide</a>.</li>
    <li>Create buckets named exactly as in the config sample:

        <ul>
            <li><code>noise_buster</code></li>
            <li><code>noise_buster_realtime</code></li>
        </ul>
    </li>
    <li>Generate an API token with write access to these buckets.</li>
    <li>Update <code>config.json</code> with your InfluxDB details.</li>
</ol>

<h3>Grafana Setup</h3>

<ol>
    <li>Install Grafana. Follow the official <a href="https://grafana.com/docs/grafana/latest/installation/">Grafana installation guide</a>.</li>
    <li>Add InfluxDB as a data source using the same credentials as in <code>config.json</code>.</li>
    <li>Import the provided Grafana dashboard JSON files to start monitoring your events quickly.</li>
    <li>Adjust queries if you have different measurement names or tags.</li>
    <li><strong>Note:</strong> The Grafana dashboard JSON files are included in the repository for your convenience.</li>
</ol>

<h2>Additional Resources</h2>

<ul>
    <li><a href="https://pushover.net/">Pushover</a> - Service for receiving push notifications.</li>
    <li><a href="https://discord.com/">Discord</a> - Communication platform with webhook support for notifications.</li>
    <li><a href="https://openweathermap.org/api">OpenWeatherMap API</a> - Service for fetching current weather data.</li>
    <li><a href="https://mqtt.org/">MQTT</a> - Lightweight messaging protocol for small sensors and mobile devices.</li>
    <li><a href="https://telraam.net/">Telraam</a> - Platform for collecting traffic data.</li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome! If you encounter issues, have suggestions, or would like to add new features:</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your changes.</li>
    <li>Submit a pull request with a detailed explanation of your changes.</li>
</ol>

<h2>Next Steps</h2>

<ul>
    <li>Adding vehicle detection using OpenCV to correlate noise events with specific vehicles.</li>
    <li>Providing a centralized InfluxDB instance for users to contribute data.</li>
    <li>Investigating other hardware options like ESP devices for sound monitoring.</li>
    <li>Implementing better data retention policies to manage database size.</li>
    <li>A dedicated YOLO-powered traffic counting script is in development and will be available soon.</li>
</ul>

<h2>License</h2>

<p>This project is licensed under the <a href="LICENSE">GNU License</a>.</p>

<h2>Project</h2>

<p>The initial project is a project by Raphael Vael.</p>

</body>
</html>
