#!/bin/sh

NOW=`date +%FT%H-%M-%S`
zip -r upload-${NOW}.zip *.py
chown 911.911 upload-${NOW}.zip
