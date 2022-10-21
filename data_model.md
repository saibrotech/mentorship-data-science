# Modelo comum de dados de vagas e empresas

## JOB
- **id:** Código da vaga - INT (AUTOINCREMENT), NOT NULL
- **title:** Título da vaga - VARCHAR (100), NOT NULL
- **date:** Data de postagem - DATE (YYYY-MM-DD), NOT NULL
- **level:** Grau de experiência - VARCHAR(20), NOT NULL
- **type:** Tipo de contratação - VARCHAR(10), NOT NULL
- **place:** Modalidade de trabalho - ENUM ('INP', 'REM', 'HYB')
- **location:** Localização da empresa - VARCHAR(100), NOT NULL
- **description:** Descrição da vaga - VARCHAR(300), NOT NULL
- **link:** Link da postagem - VARCHAR(200), NOT NULL
- **company:** Nome da empresa - VARCHAR(100), NOT NULL, FOREIGN KEY: COMPANY_id
- **category:** Categoria de vaga - ENUM('DEV', 'SUP', 'INF', 'DAT', 'SEC', 'PRD'), NOT NULL, FOREIGN_KEY: CATEGORY_id


## COMPANY
- **id:** Código da empresa - INT(AUTOINCREMENT), NOT NULL
- **name:** Nome da empresa - VARCHAR(100), NOT NULL
- **description** Descrição da empresa - VARCHAR(300)
- **website** Link da empresa - VARCHAR(200), NOT NULL
- **sector** Setor de atuação - VARCHAR(100)
- **size:** Tamanho da empresa - ENUM('S', 'M', 'L', 'XL')
- **headquarters:** Localização sede da empresa - VARCHAR(100)
- **founded:** Ano de fundação - INT(4)
- **occupation:** Serviços oferecidos - VARCHAR(200)

## CATEGORY
- **id:** Código da categoria - INT(AUTOINCREMENT), NOT NULL
- **name:** Nome da categoria - ENUM('DEV', 'SUP', 'INF', 'DAT', 'SEC', 'PRD'), NOT NULL
- **stacks:** Stacks principais - VARCHAR(300)
- **skills:** Habilidades principais - VARCHAR(300)
- **pay_min:** Piso salarial - INT
- **pay_max:** Teto salarial - INT