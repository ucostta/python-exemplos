#Formatação de Strings com várias linhas
escola = 'Senai'
curso = 'Desenvolvimento de Sistemas'
uc = 'Lógica de Programção'
matricula = 34
nota = 10
print(f"Escola: {escola}\n"
      f"Curso: {curso}\n"
      f"Unidade Curricular: {uc}"
      f"Matricula: {matricula:06d}"
      f"Nota: {nota:.2f}")