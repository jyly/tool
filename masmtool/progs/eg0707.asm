;eg0707.asm in DOS
	include io16.inc
	.code
new04h	proc	;�жϷ������
	sti
	push ax	;����Ĵ���
	push bx
	push si
	push ds
	mov ax,cs	;�����ڴ�����У���DS��CS
	mov ds,ax
	mov si,offset intmsg
dps1:	mov al,[si]
	cmp al,0
	jz dps2
	mov bx,0	;����ROM-BIOS������ʾal�е��ַ�
	mov ah,0eh
	int 10h
	inc si
	jmp dps1
dps2:	pop ds	;�ָ��Ĵ���
	pop si
	pop bx
	pop ax
	iret	;�жϷ���
intmsg  byte 0dh,0ah,'Overflow !',0
new04h	endp	;�жϷ���������
	;������ʼ
start:	mov ax,cs
	mov ds,ax	;����04H�ж�����	
	mov dx,offset new04h
	cli
	mov ax,2504h
	int 21h
	sti
	mov ax,offset tsrmsg	;��ʾ��װ��Ϣ
	call dispmsg
	mov dx,offset start	;����פ���ڴ����ĳ���
	add dx,256+15
	shr dx,4	;����Ϊ�ԡ��ڡ���16���ֽڣ�Ϊ��λ
	mov ax,3100h	;����פ��������DOS	
	int 21h
tsrmsg	byte 'INT 04H Program Installed !',0dh,0ah,0
	end start
