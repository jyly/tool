;eg0317.asm
	include io32.inc
	.data
string1	byte 'equal or not'	;first string
string2	byte 'eQual or not' 	;second string
count	equ sizeof string1
	.code
start:
	mov ecx,count
	mov esi,offset string1
	mov edi,offset string2
	cld
	repz cmpsb
	jne found
	mov al,'Y'
	jmp done
found:	mov al,'N'
done:	call dispc

	exit 0
	end start