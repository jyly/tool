;eg0803.asm for DOS
	include io16.inc
	.data
msg	byte 'What you see is what you get.',13,10,0
	.code
start:
	mov ax,@data
	mov ds,ax

	mov al,80h
	mov dx,2fbh
	out dx,al	;д��ͨ����·���ƼĴ�����ʹDLAB��1
	mov ax,96	;��Ƶϵ����1.8432MHz��(1200��16)��96��60H
	mov dx,2f8h
	out dx,al	;д������Ĵ�����8λ
	mov al,ah
 	inc dx
	out dx,al	;д������Ĵ�����8λ
	mov al,00001010b
	mov dx,2fbh
 	out dx,al	;д��ͨ����·���ƼĴ���
	mov al,13h	;ѭ�����ԣ�D4��1�� 
	mov dx,2fch	;��ֹ�жϣ�D3��0��
	out dx,al
	mov al,0	;��ֹ�����ж�
 	mov dx,2f9h
	out dx,al	;д���ж�����Ĵ�����Ӧ��֤��ʱDLAB��0��
	;
	;��ȡͨ����·״̬����ѯ����
	mov si,offset msg	; SIָ������Ϣ
	mov bx,1	; BX��1��ʾ��Ҫ������Ϣ
	mov cx,1	; CX��1��ʾ���Խ�����Ϣ
statue:	mov ax,bx
	or ax,cx	; BX��CX��0����ʾ���պͷ��Ͷ���ɣ�ת�����
	jz done
	mov dx,2fdh	; ��ȡͨ����·״̬�Ĵ���
	in al,dx
	test al,1eh	; �����д����?
	jz statue1	; û�д��󣬼���
	; �����д����屨��
	mov dx,2f8h	; ����������������ݣ�����
	in al,dx
	mov al,07h	; ������Ƶ�ASCII��Ϊ07H
	call dispc
	jmp statue	; ������ѯ
statue1:	test al,01h	; ���յ�������?
	jz statue2	; û���յ����ݣ�����
	; �ѽ����ַ�����ȡ���ַ�����ʾ������ǽ�β�ַ��������ñ�־��
	mov dx,2f8h	; �����뻺��Ĵ�����ȡ�ַ�
	in al,dx
	cmp al,0	; �ǽ�β�ַ��� 
	jnz receive
	xor cx,cx	; CX��0�����ٽ�������
	jmp statue	; ������ѯ
receive:	and al,7fh	; ���ͱ�׼ASCII�룬����7������λ�����Խ�ȡ��7λ
	call dispc	; ��Ļ��ʾ������
	jmp statue	; ������ѯ
statue2:	cmp bx,1	; ����Ҫ���͵��ַ���
	jne statue	; �޷����ַ���������ѯ
	test al,20h	; ���ּĴ����գ���������ݣ���?
	jz statue	; ���������������ѯ
	; ���ּĴ����ѿգ����Է�������
	mov al,[si]	; ���Ҫ���͵��ַ�
	inc si
	cmp al,0	; �ǽ�β�ַ���
	jnz transmit 
	xor bx,bx	; �޷����ַ�������BX��0
	jmp statue	; ������ѯ
transmit:	mov dx,2f8h	; ���ַ���������ͱ��ּĴ���
	out dx,al	; ���з�������
	jmp statue	; ������ѯ
done:		
	exit 0
	end start
