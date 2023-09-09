from config import Config, set_values_from_jsonobj, AvailableOptions
import argparse

def main():
    # print all class variables of Config class
    #print(Config.options)
    #print(AvailableOptions("enable_feature3")) # if value not there gives error, else gives the enum itself AO.EF2 in short
    if AvailableOptions.ENABLE_FEATURE1 in Config.options:
        print("Feature 1 is enabled!")
        print(Config.dataset_path)
    elif AvailableOptions.ENABLE_FEATURE2 in Config.options:
        print("Feature 2 is enabled!")
        print(Config.dataset_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", type=str, default="config.json", required=True)
    args = parser.parse_args()

    set_values_from_jsonobj(args.config_file)
    main()