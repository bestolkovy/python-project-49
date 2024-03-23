install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain_even

bpp:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --force-reinstall  dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install  dist/*.whl

lint:
	poetry run flake8 brain_games

virt:
	source .venv/bin/activate



