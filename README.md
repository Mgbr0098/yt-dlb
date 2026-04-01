# yt-dlb

Uma ferramenta compatível com `yt-dlp` baseada em Python, projetada para reexportar toda a funcionalidade da biblioteca `yt-dlp`.

## Instalação

### 1) Instalação no Linux/macOS/Windows

```bash
git clone https://github.com/Mgbr0098/yt-dlb.git
cd yt-dlb
python -m pip install --upgrade pip
python -m pip install -e .
```

Depois disso, você tem:
- `yt-dlb`
- `yt-dlb-interactive`

### 2) Instalação no Termux (Android)

```bash
pkg update -y && pkg upgrade -y
pkg install python git ffmpeg -y
termux-setup-storage
cd ~
git clone https://github.com/Mgbr0098/yt-dlb.git
cd yt-dlb
python -m pip install --upgrade pip
python -m pip install -e .
```

### 3) Verificar instalação

```bash
yt-dlb --version
yt-dlb --help
yt-dlb-interactive --help
```

## Uso

```bash
yt-dlb https://www.youtube.com/watch?v=dQw4w9WgXcQ
yt-dlb -F https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Como funciona

O pacote chama o entrypoint `yt_dlp.main()` diretamente, então quase todas as opções e features do `yt-dlp` são suportadas.

## Uso interativo

O utilitário também oferece uma interface interativa para baixar por termo/URL e escolher diretório de saída:

```bash
yt-dlb --interactive
# ou
yt-dlb -i
# e também
yt-dlb-interactive
```

Na interface, você pode:
- informar uma URL de vídeo ou termo de pesquisa (ex: `Rick Astley`)
- apontar para um arquivo com uma lista de URLs/consultas (uma por linha)
- escolher diretório de saída
- escolher formato: vídeo+áudio ou somente áudio (MP3)

## Desenvolvimento

- Confira o repositório
- Instale com `pip install -e .`
- Execute `yt-dlb --help`
- Para testar internamente, rode `python -m yt_dlb --help`

