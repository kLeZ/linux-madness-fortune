# Linux Madness Fortune

Una raccolta di oltre 300 frasi sarcastiche, offensive e umoristiche sul mondo Linux, DevOps e AI, per il programma `fortune`.

## Installazione manuale

```bash
./install.sh
````

Installa localmente (se utente normale) o globalmente (se root).

## Uso

```bash
fortune linux_madness
```

Per effetti epici, prova:

```bash
fortune linux_madness | cowsay | lolcat
```

## Build RPM con OBS

* Il pacchetto è pensato per essere costruito con Open Build Service (OBS).
* Usa `osc` per caricare sorgenti e controllare lo stato build.
* `.spec` è configurato per versioni 1.0 e nome `linux-madness-fortune`.

## Licenza

WTFPL - Do What The Fuck You Want To Public License
