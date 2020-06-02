#!/usr/bin/env bash
#
# This file is generated by l2tdevtools update-dependencies.py any dependency
# related changes should be made in dependencies.ini.

# Exit on error.
set -e

export DEBIAN_FRONTEND=noninteractive

# Dependencies for running ${project_name}, alphabetized, one per line.
# This should not include packages only required for testing or development.
${python_dependencies}

# Additional dependencies for running tests, alphabetized, one per line.
${test_dependencies}

# Additional dependencies for development, alphabetized, one per line.
${development_dependencies}

# Additional dependencies for debugging, alphabetized, one per line.
${debug_dependencies}

sudo add-apt-repository ppa:gift/dev -y
sudo apt-get update -q
sudo apt-get install -y $${PYTHON_DEPENDENCIES}

if [[ "$$*" =~ "include-debug" ]]; then
    sudo apt-get install -y $${DEBUG_DEPENDENCIES}
fi

if [[ "$$*" =~ "include-development" ]]; then
    sudo apt-get install -y $${DEVELOPMENT_DEPENDENCIES}
fi

if [[ "$$*" =~ "include-test" ]]; then
    sudo apt-get install -y $${TEST_DEPENDENCIES}
fi
