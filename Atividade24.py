paisA = 80000
paisB = 200000
ano = 0

while paisA < paisB:
   paisA += int(paisA * 0.03)
   paisB += int(paisB * 0.0015)
   ano += 1

print(f"a população do pais A passara a do pais B em {ano} anos")