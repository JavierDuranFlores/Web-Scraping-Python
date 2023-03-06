#!/bin/bash
echo "Corriendo ..."
python scraping-coppel.py
python scraping-mercado-libre.py
python scraping-att.py
python scraping-ebay.py
