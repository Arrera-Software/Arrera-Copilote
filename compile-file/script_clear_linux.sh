pip uninstall -y llama-cpp-python

CMAKE_ARGS="-DGGML_CUDA=off" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir --no-binary llama-cpp-python