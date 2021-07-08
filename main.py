import os

os.system('sed -i "s|PORT|$PORT|" application.yml')

password = os.environ.get("PASSWORD")

os.system(f'sed -i "s|PASSWORD|{"$PASSWORD" if password else "youshallnotpass"}|" application.yml')

options = os.environ.get("JAVA_TOOL_OPTIONS")

os.system(f'java -jar Lavalink.jar {options}')