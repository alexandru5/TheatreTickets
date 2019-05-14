#!/bin/bash
cd ./database && sudo ./loaddb.sh && cd ../tickets && sudo ./loadserver.sh
