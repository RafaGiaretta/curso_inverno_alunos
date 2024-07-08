## Guia de contribuição

Este é um projeto feito para os alunos do curso de inverno da UNILINS.

Alem de contribuir com seu Profile README, tambem é esperado: 

⚠️ Ajudando em outros Profiles com sugestoes de melhorias

⭐ Adicionando este respositorio aos favoritos **(star)**

---

## Contribuindo no diretório "ALUNOS"

A contribuição neste diretório é a forma de voce completar o desafio pratico da aula 1, "Desenvolvimento de software colaborativo com Git e GitHub"

Para isso, você deve criar seu Profile README.md, se apresentando, indicando suas habilidades, utilizar cards com suas estatísticas no GitHub e projetos que criou, colaborou ou deseje receber colaboração.

### 1) Faça um Fork  deste Repositório

Acesse a página principal do repositório e clique no botão "Fork" no canto superior direito da página: 

<img src="https://i.ibb.co/8zz39vy/Captura-de-tela-2024-07-07-171941.png" alt="Imagem como fazer Fork" >

### 2) Clone localmente

Atraves do GitBash ou VSCODE, digite o comando git clone, seguido da URL do seu fork para clonar o seu repositório localmente, Exemplo:

git clone https://github.com/SEU_USERNAME/curso_inverno_alunos.git

Precione enter, e será criado uma cópia do seu fork localmente.

### 3) Crie uma nova branch

Utilize o comando git checkout -b para criar e alternar para a nova branch e a nomeie como `feat/ALUNOS/SEU_USERNAME`

### 4) Crie o seu Profile README

Dentro da pasta ALUNOS, crie um arquivo em Markdown (extensão .md) e nomeie com o mesmo nome de usuário do  GitHub.

##### 4.1) Desenvolva seu Profile REAME.md

Para isso, você pode utilizar como exemplo os nossos Profile [RafaGiaretta](https://github.com/RafaGiaretta), [GuilhermeDevSoftware](https://github.com/GuilhermeDevSoftware) e adicionar alguns dos utilitários presentes na pasta [`utils`](https://github.com/RafaGiaretta/curso_inverno_alunos/tree/main/ALUNOS/utils) 


### 5) Adicione suas alterações à "STAGING AREA"
Utilize o comando `git add community/SEU_USERNAME.md` para adicionar sua alteração no Git.

### 6) Crie um community

Crie um comit e adicione  a mensagem indicando a adição do seu perfil: 
```bash
git commit -m"feat: add SEU_USERNAME profile"
```
## IMPORTANTE 
> Verifique a [`Convenção de Commits`](https://github.com/digitalinnovationone/dio-lab-open-source/blob/main/CONTRIBUTING.md#conven%C3%A7%C3%A3o-de-commits) 

### 7) Envie as Alterações para o seu Repositório Remoto
Envie as alterações realizadas localmente para a branch `feat/community/SEU_USERNAME` no seu repositório remoto com o comando: 
```bash
git push origin feat/community/SEU_USERNAME
```

### 8) Crie um  **Pull Request**
Atente-se que o nome do seu arquivo deve ser exatamente ao nome de usuário do GitHub.
 Caso precise de ajuda clique em [Como criar uma solicitação de pull](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)


## Convenção de Commits 

| Tipo de Commit |Descrição                                                            | Exemplo
| ---------------|----------------------------------------------------------------------|-----------
| `feat`         | Adiciona uma nova funcionalidade ao projeto.                         | `feat: add USENAME.md profile`
| `fix`          | Corrige um bug ou problema no projeto.                               | `fix: fixed issue fix#IssueNumber`
| `docs`         | Altera a documentação do projeto.| `docs: update README.md`
| `style`        | Realiza mudanças na aparência, sem alterar a funcionalidade.         | `style: add EFFECTNAME to COMPONENT`
| `refactor`     | Realiza mudanças no código que não alteram a funcionalidade.         | `refactor: refactor at CLASSNAME`
| `test`         | Adiciona ou modifica testes no projeto.                              | `test: add unit test for UserService`


## Referências
- [ANGULAR. Contributing to Angular](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md)
- [CONVENTIONAL COMMITS. Summary](https://www.conventionalcommits.org/en/v1.0.0/)
- [GITHUB. Configurar diretrizes para os contribuidores do repositório](https://docs.github.com/pt/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [DIO](https://web.dio.me/)
