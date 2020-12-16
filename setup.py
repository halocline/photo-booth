import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="photo-booth",  # Replace with your own username
    version="0.0.1",
    author="Matt Glissmann",
    author_email="mdglissmann@gmail.com",
    description="raspberry pi based photo booth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/halocline/photo-booth",
    packages=setuptools.find_packages(),
    install_requires=[
        'google-assistant-library>=1.0.1',
        'google-assistant-grpc>=0.2.0',
        'google-auth>=1.5.1',
        'google-auth-oauthlib>=0.2.0',
        'google-cloud-speech>=0.36.0',
        'gpiozero',
        'protobuf>=3.6.1',
        'picamera',
        'Pillow',
        'RPi.GPIO',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
