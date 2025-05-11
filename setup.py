from setuptools import setup, find_packages

setup(
    name="auroraai",
    version="0.1.0",
    author="Your Name",
    description="AuroraAI: Voice-driven AI assistant with Electron UI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sounddevice",
        "faster_whisper",
        "google-generativeai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "auroraai = backend.cli:main",
        ],
    },
    package_data={
        "": ["electron/**/*"],
    },
)
