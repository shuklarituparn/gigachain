import certifi
import httpx


def install_russian_certs():
    """Установка корневого сертификата Минцифры России."""
    url = f"https://gu-st.ru/content/Other/doc/russian_trusted_root_ca.cer"

    with open(certifi.where()) as infile:
        installed = url in infile.read()

    if installed:
        exit("ERR: Сертификат Минцифры России уже установлен!")
    else:
        response = httpx.get(url, verify=False)
        response.raise_for_status()
        with open(certifi.where(), "ba") as outfile:
            outfile.write(b"\n\n# --- BEGIN %s ---\n\n" % url.encode())
            outfile.write(response.content.replace(b"\r\n", b"\n"))
            outfile.write(b"\n\n# --- END %s ---\n\n" % url.encode())
        print("Сертификат Минцифры России - установлен!")


if __name__ == "__main__":
    # python -m gigachain
    install_russian_certs()
