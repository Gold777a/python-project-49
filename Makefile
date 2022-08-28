install: #обновление зависимостей
	poetry install

brain-games: #запуск проекта через make
	poetry run brain-games

build: #сборка проекта
	poetry build

publish: #публикация
	poetry publish --dry-run

package-install: #сборка пакета в whl
	python3 -m pip install --user dist/*.whl


lint: 
	poetry run flake8 brain_games

