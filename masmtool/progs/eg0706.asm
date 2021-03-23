;eg0706.asm in DOS
	include io16.inc
	.data
intmsg	byte  'A 8259A Interrupt !',0dh,0ah,0
counter	byte 0	;�жϴ�����¼��Ԫ
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3508h	;��ȡԭ�ж�����
	int 21h
	push es	;����ԭ�ж����������ö�ջ��
	push bx
	cli	;���ж�
	push ds	;�������ж����� 
	mov ax,seg new08h
	mov ds,ax
	mov dx,offset new08h
	mov ax,2508h
	int 21h
	pop ds
	in al,21h	;����IMR
	push ax	;����ԭIMR����
	and al,0feh	;����IRQ0����������
	out 21h,al	;������IMR����	
	mov counter,0	;�����жϴ�����ֵ
	sti	;���ж�
	;����������жϷ���������ã����Դ�����������
start1:	cmp counter,10	;�������������ѭ���ȴ��ж�
	jb start1	;�ж�10���˳�
	;
	cli	;���ж�
	pop ax	;�ָ�IMR
	out 21h,al
	pop dx	;�ָ�ԭ�ж�����
	pop ds
	mov ax,2508h
	int 21h
	sti	;���ж�
	exit 0

	; �жϷ������
new08h	proc 
	sti	;���ж�
	push ax	;�����Ĵ���
	push si
	push ds
	mov ax,@data	;�ⲿ��������жϣ�DSҲ��ȷ�������Ա�������DS
	mov ds,ax
	inc counter	;�жϴ�����1
	mov si,offset intmsg	;��ʾ��Ϣ
	call dpstri 
	mov al,20h	;����EOI����
	out 20h,al
	pop ds	;�ָ��Ĵ���
	pop si
	pop ax
	iret	;�жϷ���
new08h	endp
dpstri	proc	;��ʾ�ַ����ӳ���
	push ax	;��ڲ�����DS:SI���ַ�����ַ
	push bx
dps1:	mov al,[si]
	cmp al,0
	jz dps2
	mov bx,0	;����ROM-BIOS������ʾal�е��ַ�
	mov ah,0eh
	int 10h
	inc si
	jmp dps1
dps2:	pop bx
	pop ax
	ret
dpstri	endp

	end start
