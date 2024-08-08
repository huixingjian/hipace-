#! /usr/bin/env bash

# This file is part of the HiPACE++ test suite.
# It runs a Hipace simulation in SI units
# Initialize a chirped pulse and test the factors by python scripts.


# abort on first encounted error
set -eu -o pipefail

# Read input parameters
HIPACE_EXECUTABLE=$1
HIPACE_SOURCE_DIR=$2

HIPACE_EXAMPLE_DIR=${HIPACE_SOURCE_DIR}/examples/laser
HIPACE_TEST_DIR=${HIPACE_SOURCE_DIR}/tests

FILE_NAME=`basename "$0"`
TEST_NAME="${FILE_NAME%.*}"

# chirp parameters
CHIRP_VAL = 2.4e-26


# Run the simulation
mpiexec -n 1 $HIPACE_EXECUTABLE $HIPACE_EXAMPLE_DIR/inputs_SI \
        laser.beta = CHIRP_VAL
        laser.zeta = CHIRP_VAL
        laser.beta = CHIRP_VAL

# Compare the results within python script
 
