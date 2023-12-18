import requests

def is_real(filename, checksum) -> bool:
    generated_checksum = ''.join([char for char in filename if filename.count(char) == 1])
    return generated_checksum == checksum

response = requests.get('https://codember.dev/data/files_quarantine.txt')
lines = response.text.split('\n')
real_files = []

for line in lines:
    filename, checksum = line.split('-')
    if is_real(filename, checksum):
        real_files.append(filename)

print(real_files[32])
