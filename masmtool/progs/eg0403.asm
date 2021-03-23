;eg0403.asm
	include io32.inc
	.data
no_msg	byte 'Not Ready!',0
yes_msg	byte 'Ready to Go!',0
	.code
start:
	mov eax,56h	;假设一个数据
	test eax,02h	;测试D1位，用10B与其进行逻辑与
	jz nom	;D1＝0（ZF＝1），转移到NOM
	mov eax,offset yes_msg
	jmp done	;无条件转移，跳过另一个分支
nom:	mov eax,offset no_msg
done:	call dispmsg

	exit 0
	end start
