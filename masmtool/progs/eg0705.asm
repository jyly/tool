;eg0705.asm in DOS
	include io16.inc
	.data
intoff	word ?	;���ڱ���ԭ�жϷ�������ƫ�Ƶ�ַ
intseg	word ? 	;���ڱ���ԭ�жϷ������Ķε�ַ
intmsg	byte 'A Instruction Interrupt !',0dh,0ah,0	;�ַ�������0��β��
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3580h	;��ȡϵͳ��ԭ80H�ж�����
	int 21h
	mov intoff,bx	;����ƫ�Ƶ�ַ
	mov intseg,es	;����λ���ַ
	push ds
	mov dx,offset new80h
	mov ax,seg new80h
	mov ds,ax
	mov ax,2580h	;���ñ������80H�ж�����
	int 21h
	pop ds
	;
	mov dx,offset intmsg	;������ڲ���DS��DX
	int 80h	;����80H�жϷ��������ʾ�ַ���
	;
	mov dx,intoff	;�ָ�ϵͳ��ԭ80H�ж�����
	mov ax,intseg	;ע��������DX��������DS��ڲ���
	mov ds,ax	;��Ϊ�ȸı���DS���Ͳ���׼ȷȡ��intoff����ֵ
	mov ax,2580h
	int 21h
	exit 0

	;80H�ڲ��жϷ��������ʾ�ַ�������0��β����DS��DX���������׵�ַ
new80h	proc	;���̶���
	sti	;���ж�
	push ax	;�����Ĵ���
	push bx
	push si
	mov si,dx
new1:	mov al,[si]	;��ȡ����ʾ�ַ�
	cmp al,0	;Ϊ��0������
	jz new2
	mov bx,0	;����ROM-BIOS������ʾһ���ַ�
	mov ah,0eh
	int 10h
	inc si	;��ʾ��һ���ַ�
	jmp new1
new2:	pop si	;�ָ��Ĵ���
	pop bx
	pop ax
	iret	;�жϷ���
new80h	endp	;�жϷ���������

	end start
