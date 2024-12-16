import torch

import qai_hub as hub
from qai_hub_models.models.openai_clip import CLIPTextEncoder,CLIPImageEncoder

# Load the model
text_encoder_model = CLIPTextEncoder.from_pretrained()
image_encoder_model = CLIPImageEncoder.from_pretrained()

# Device
device = hub.Device("Samsung Galaxy S23")
# Trace model
text_encoder_input_shape = text_encoder_model.get_input_spec()
text_encoder_sample_inputs = text_encoder_model.sample_inputs()

traced_text_encoder_model = torch.jit.trace(text_encoder_model, [torch.tensor(data[0]) for _, data in text_encoder_sample_inputs.items()])

# Compile model on a specific device
text_encoder_compile_job = hub.submit_compile_job(
    model=traced_text_encoder_model ,
    device=device,
    input_specs=text_encoder_model.get_input_spec(),
)

# Get target model to run on-device
text_encoder_target_model = text_encoder_compile_job.get_target_model()
# Trace model
image_encoder_input_shape = image_encoder_model.get_input_spec()
image_encoder_sample_inputs = image_encoder_model.sample_inputs()

traced_image_encoder_model = torch.jit.trace(image_encoder_model, [torch.tensor(data[0]) for _, data in image_encoder_sample_inputs.items()])

# Compile model on a specific device
image_encoder_compile_job = hub.submit_compile_job(
    model=traced_image_encoder_model ,
    device=device,
    input_specs=image_encoder_model.get_input_spec(),
)

# Get target model to run on-device
image_encoder_target_model = image_encoder_compile_job.get_target_model()