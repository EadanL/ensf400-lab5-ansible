import subprocess
import time
import ansible_runner

def main():
    docker_compose_up()
    time.sleep(3) # without sleep the conatiners don't have enough time to setup and will cause the playbook to fail
    r = ansible_runner.run(private_data_dir='./', playbook='hello.yml', inventory='hosts.yml', envvars={'ANSIBLE_CONFIG': 'ansible.cfg'})
    print("{}: {}".format(r.status, r.rc))
    for each_host_event in r.events:
        print(each_host_event['event'])
    print("******Final status: ******")
    print(r.stats)

def docker_compose_up():
    try:
        # Run the command using subprocess
        subprocess.run(['docker-compose', 'up', '-d'], check=True)
        print("Docker Compose up completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running docker-compose: {e}")


if __name__ == "__main__":
    main()
