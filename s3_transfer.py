import boto3, json, os

def main():
    try:
        with open("/etc/config.json") as f:
            config = json.load(f)
            ACCESS_KEY_ID = config["S3_ACCESS_KEY_ID"]
            SECRET_ACCESS_KEY = config["S3_SECRET_ACCESS_KEY"]
            BUCKET_NAME = config["S3_BUCKET_NAME"]
    except (FileNotFoundError, KeyError):
        try:
            with open("config.json") as f:
                config = json.load(f)
                ACCESS_KEY_ID = config["S3_ACCESS_KEY_ID"]
                SECRET_ACCESS_KEY = config["S3_SECRET_ACCESS_KEY"]
                BUCKET_NAME = config["S3_BUCKET_NAME"]
        except (FileNotFoundError, KeyError):
            print("FileNotFoundError or KeyError")
            return

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    directory = "./media/samples"
    for filename in os.listdir(directory):
        if filename[-3:] == "png":
            filepath = os.path.join(directory, filename)
            s3_dir = os.path.join("init/", filename)
            s3.upload_file(filepath, BUCKET_NAME, s3_dir)

if __name__ == "__main__":
    main()