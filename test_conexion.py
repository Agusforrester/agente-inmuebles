from curl_cffi import requests as cffi_requests

url = "https://www.zonaprop.com.ar/departamentos-venta-belgrano-r-belgrano.html"
respuesta = cffi_requests.get(url, impersonate="chrome")

print("Código de estado:", respuesta.status_code)
print("Tamaño del HTML:", len(respuesta.text), "caracteres")
