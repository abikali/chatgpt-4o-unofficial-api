"""
Status display module for ChatGPT 4o API.
"""

import time
import random
from typing import Dict, Any, Optional
from .image_processor import ImageProcessor

class StatusDisplay:
    """Handles real-time status display for image generation."""

    def __init__(self):
        self._processor = ImageProcessor()
        self._current_step = 0
        self._total_steps = 9
        self._start_time = 0
        self._last_update = 0

    def start_generation(self, request_data: Dict[str, Any], request_id: str) -> None:
        """Start the image generation process and display status."""
        self._start_time = time.time()
        self._last_update = self._start_time

        self._display_header(request_data, request_id)

        # Initialize model
        self._processor.initialize_model(request_data)
        self._update_status("Initializing model")

        # Load weights
        self._processor.load_weights()
        self._update_status("Loading weights")

        # Process prompt
        prompt_data = self._processor.process_prompt(request_data["prompt"])
        self._update_status("Processing prompt")

        # Generate image data
        image_data = self._processor.generate_image_data(prompt_data)
        self._update_status("Generating image data")

        # Optimize parameters
        params = self._processor.optimize_parameters(image_data)
        self._update_status("Optimizing parameters")

        # Apply style transfer
        style_data = self._processor.apply_style_transfer(image_data, request_data["style"])
        self._update_status("Applying style transfer")

        # Post-process
        post_data = self._processor.post_process(style_data)
        self._update_status("Post-processing")

        # Enhance quality
        quality_data = self._processor.enhance_quality(post_data, request_data["quality"])
        self._update_status("Quality enhancement")

        # Finalize
        final_data = self._processor.finalize_output(quality_data)
        self._update_status("Finalizing output")

        self._display_completion()

    def _display_header(self, request_data: Dict[str, Any], request_id: str) -> None:
        """Display the header with request information."""
        model = request_data.get("model", "gpt-4o-image")
        size = request_data.get("size", "1024x1024")
        quality = request_data.get("quality", "standard")

        print("\n" + "="*50)
        print("""
    ╔═══════════════════════════════════════╗
    ║  🎨  Image Generation in Progress     ║
    ║                                     ║
    ║  Model: {model:<30} ║
    ║  Size: {size:<31} ║
    ║  Quality: {quality:<27} ║
    ║  Request ID: {request_id:<23} ║
    ║                                     ║
    ║  🚀  Starting generation...         ║
    ║                                     ║
    ║  ⏳  Estimated time: {time:<25} ║
    ║  🎉  Processing...                  ║
    ╚═══════════════════════════════════════╝
        """.format(
            model=model,
            size=size,
            quality=quality,
            request_id=request_id,
            time=f"{random.uniform(2.5, 4.5):.1f}s"
        ))
        print("="*50 + "\n")

    def _update_status(self, step: str) -> None:
        """Update the status display with current step."""
        self._current_step += 1
        elapsed = time.time() - self._last_update
        self._last_update = time.time()

        print(f"    ║  ✓ {step:<30} ║")
        print(f"    ║  ⏱️  Step time: {elapsed:.1f}s{' ' * 15} ║")
        print("    ║                                     ║")

    def _display_completion(self) -> None:
        """Display completion message."""
        total_time = time.time() - self._start_time
        print(f"""
    ║                                     ║
    ║  ✅ Generation completed!           ║
    ║  ⏱️  Total time: {total_time:.1f}s            ║
    ║  🎉  Image ready for download      ║
    ╚═══════════════════════════════════════╝
        """)
