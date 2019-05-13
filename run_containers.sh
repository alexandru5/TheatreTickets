#!/bin/bash
cd ./db && sudo ./loaddb.sh && cd ../tickets && sudo ./loadserver.sh
