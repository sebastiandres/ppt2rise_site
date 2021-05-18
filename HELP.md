# HELP

# Install requirements with Conda

## Crear el ambiente
conda create -n polite_survey

## Instalar librerías
source activate polite_survey
pip install -r requirements.txt

# Desactivar ambiente
conda deactivate

## Borrar el ambiente
conda env remove -n polite_survey

## Mostrar todos los ambientes
conda env list

# Install requirements with a virtual environment 

## Crear el ambiente
virtualenv venv

## Activar ambiente 
source venv/bin/activate

## Instalar librerías
pip install -r requirements.txt

## Desactivar Ambiente
deactivate

## Borrar el ambiente
rm -rf venv/

## Lanzar en local
gunicorn --config gunicorn_config.py app:app

## Lanzar en server (Segun ProcFile)
gunicorn --worker-tmp-dir /dev/shm --config gunicorn_config.py app:app


