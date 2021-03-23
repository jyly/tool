;eg0311.asm
	include io32.inc
	.data
qvar1	qword 6778300082347856h
qvar2	qword 6776200012348998h
	.code
start:
	mov eax,dword ptr qvar1
	add eax,dword ptr qvar2
	mov edx,dword ptr qvar1+4
	adc edx,dword ptr qvar2+4
	call disprd

	exit 0
	end start