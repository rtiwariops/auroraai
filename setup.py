from setuptools import setup, find_packages

setup(
    name="auroraai",
    version="0.1.0",
    description="Voice-driven AI assistant for live transcription and streaming answers.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Robbie Tiwari",
    author_email="rtiwariops@gmail.com",
    url="https://github.com/rtiwariops/auroraai",
    packages=find_packages(include=["backend", "backend.*"]),
    include_package_data=True,
    install_requires=[
        "openai-whisper",
        "pyaudio",
        "numpy",
        "requests",
        # Add any other required dependencies
    ],
    entry_points={
        "console_scripts": [
            "auroraai=backend.__main__:main",  # Adjust if your main entry is elsewhere
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.7',
)
