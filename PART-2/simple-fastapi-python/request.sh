#!/bin/bash
for i in {1..1000}
do
  curl http://localhost:30003
  echo " ====> $i requests completed"
done

#local would be port 8000