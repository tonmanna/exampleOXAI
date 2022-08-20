#!/bin/bash
docker run --rm -it -v /${PWD}/analysis:/project/analysis -v /${PWD}/templates:/project/templates -v /${PWD}/nlp:/project/nlp -p 8080:8080 nlp

