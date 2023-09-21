L2:
	li v0,5
	ecall
	storerv(v0,_)
L3:
	loadvr(1, t1)
	storerv(t1,fact)
L4:
	loadvr(1, t1)
	storerv(t1,i)
L5:
	loadvr(i,t1)
	loadvr(i,t2)
	ble,t1,t2,7
L6:
	b 12
L8:
	loadvr(T_1, t1)
	storerv(t1,fact)
L10:
	loadvr(T_2, t1)
	storerv(t1,i)
L11:
	b 5
L12:
	li v0,1
	loadvr(_,a0)
	ecall
L15:
	loadvr(x,t1)
	loadvr(x,t2)
	ble,t1,t2,17
L16:
	b 19
L17:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L18:
	b 29
L20:
	loadvr(T_3, t0)
	sw t0, -(12+4i)(fp)
L21:
	gnlvcode(T_4)
	lw t0,(t0)
	sw t0, -(12+4i)(fp)
L22:
	lw t0,-4(sp)
	sw t0,-4(fp)
L24:
	loadvr(T_5, t0)
	sw t0, -(12+4i)(fp)
L25:
	gnlvcode(T_6)
	lw t0,(t0)
	sw t0, -(12+4i)(fp)
L26:
	lw t0,-4(sp)
	sw t0,-4(fp)
L28:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L31:
	li v0,5
	ecall
	storerv(v0,_)
L32:
	loadvr(x, t0)
	sw t0, -(12+4i)(fp)
L33:
	gnlvcode(T_8)
	lw t0,(t0)
	sw t0, -(12+4i)(fp)
L34:
	lw t0,-4(sp)
	sw t0,-4(fp)
L35:
	li v0,1
	loadvr(_,a0)
	ecall
L38:
	li v0,5
	ecall
	storerv(v0,_)
L39:
	loadvr(0, t1)
	storerv(t1,count)
L40:
	loadvr(x,t1)
	loadvr(x,t2)
	bgt,t1,t2,42
L41:
	b 47
L43:
	loadvr(T_9, t1)
	storerv(t1,x)
L45:
	loadvr(T_10, t1)
	storerv(t1,count)
L46:
	b 40
L47:
	li v0,1
	loadvr(_,a0)
	ecall
L53:
	b 56
L54:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L55:
	b 57
L56:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L59:
	loadvr(2, t1)
	storerv(t1,i)
L60:
	loadvr(i,t1)
	loadvr(i,t2)
	blt,t1,t2,62
L61:
	b 73
L62:
	loadvr(i, t0)
	sw t0, -(12+4i)(fp)
L63:
	loadvr(x, t0)
	sw t0, -(12+4i)(fp)
L64:
	gnlvcode(T_13)
	lw t0,(t0)
	sw t0, -(12+4i)(fp)
L65:
	lw t0,-4(sp)
	sw t0,-4(fp)
L67:
	b 70
L68:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L69:
	b _
L71:
	loadvr(T_14, t1)
	storerv(t1,i)
L72:
	b 60
L73:
	loadvr(_, t1)
	lw t0,-8(sp)
	sw t1,(t0)
L76:
	loadvr(2, t1)
	storerv(t1,i)
L77:
	loadvr(i,t1)
	loadvr(i,t2)
	ble,t1,t2,79
L78:
	b 87
L79:
	loadvr(i, t0)
	sw t0, -(12+4i)(fp)
L80:
	gnlvcode(T_15)
	lw t0,(t0)
	sw t0, -(12+4i)(fp)
L81:
	lw t0,-4(sp)
	sw t0,-4(fp)
L83:
	b 86
L84:
	li v0,1
	loadvr(_,a0)
	ecall
L85:
	b _
L86:
	b 77
L88:
	loadvr(T_16, t1)
	storerv(t1,i)
L91:
	lw t0,-4(sp)
	sw t0,-4(fp)
L92:
	lw t0,-4(sp)
	sw t0,-4(fp)
L93:
	lw t0,-4(sp)
	sw t0,-4(fp)
L94:
	lw t0,-4(sp)
	sw t0,-4(fp)
