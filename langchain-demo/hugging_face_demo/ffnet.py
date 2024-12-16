from datasets import load_dataset

# Use input resolution of the network
input_shape = (1, 3, 1024, 2048)

# Load 100 RGB images of urban scenes 
dataset = load_dataset("UrbanSyn/UrbanSyn", 
                split="train", 
                data_files="rgb/*_00*.png")
dataset = dataset.train_test_split(1)

# Hold out for testing
calibration_dataset = dataset["train"]
test_dataset = dataset["test"]