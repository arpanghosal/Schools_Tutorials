# This file was automatically created by FeynRules =.2.2
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (January 24, 2013)
# Date: Sat 23 Aug 2014 21:29:06


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.uv] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_155_36,(0,0,1):C.R2GC_155_37})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.uv] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_102_5,(2,0,1):C.R2GC_102_6,(0,0,0):C.R2GC_102_5,(0,0,1):C.R2GC_102_6,(4,0,0):C.R2GC_100_1,(4,0,1):C.R2GC_100_2,(3,0,0):C.R2GC_100_1,(3,0,1):C.R2GC_100_2,(8,0,0):C.R2GC_101_3,(8,0,1):C.R2GC_101_4,(7,0,0):C.R2GC_106_12,(7,0,1):C.R2GC_160_43,(6,0,0):C.R2GC_105_10,(6,0,1):C.R2GC_161_44,(5,0,0):C.R2GC_100_1,(5,0,1):C.R2GC_100_2,(1,0,0):C.R2GC_100_1,(1,0,1):C.R2GC_100_2,(11,3,0):C.R2GC_104_8,(11,3,1):C.R2GC_104_9,(10,3,0):C.R2GC_104_8,(10,3,1):C.R2GC_104_9,(9,3,1):C.R2GC_103_7,(2,1,0):C.R2GC_102_5,(2,1,1):C.R2GC_102_6,(0,1,0):C.R2GC_102_5,(0,1,1):C.R2GC_102_6,(6,1,0):C.R2GC_157_39,(6,1,1):C.R2GC_157_40,(4,1,0):C.R2GC_100_1,(4,1,1):C.R2GC_100_2,(3,1,0):C.R2GC_100_1,(3,1,1):C.R2GC_100_2,(8,1,0):C.R2GC_101_3,(8,1,1):C.R2GC_159_42,(7,1,0):C.R2GC_106_12,(7,1,1):C.R2GC_106_13,(5,1,0):C.R2GC_100_1,(5,1,1):C.R2GC_100_2,(1,1,0):C.R2GC_100_1,(1,1,1):C.R2GC_100_2,(0,2,0):C.R2GC_102_5,(0,2,1):C.R2GC_102_6,(2,2,0):C.R2GC_102_5,(2,2,1):C.R2GC_102_6,(5,2,0):C.R2GC_100_1,(5,2,1):C.R2GC_100_2,(1,2,0):C.R2GC_100_1,(1,2,1):C.R2GC_100_2,(7,2,0):C.R2GC_158_41,(7,2,1):C.R2GC_102_6,(4,2,0):C.R2GC_100_1,(4,2,1):C.R2GC_100_2,(3,2,0):C.R2GC_100_1,(3,2,1):C.R2GC_100_2,(8,2,0):C.R2GC_101_3,(8,2,1):C.R2GC_156_38,(6,2,0):C.R2GC_105_10,(6,2,1):C.R2GC_105_11})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.uv__tilde__, P.uv, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.uv] ] ],
               couplings = {(0,0,0):C.R2GC_110_17})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.uv__tilde__, P.u, P.p2 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.g, P.u, P.uv] ] ],
               couplings = {(0,0,0):C.R2GC_172_47})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.uv__tilde__, P.u, P.p1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.g, P.u, P.uv] ] ],
               couplings = {(0,0,0):C.R2GC_171_46})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_148_28,(0,1,0):C.R2GC_149_29})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_139_24})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_138_23})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_151_31})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_152_32})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_150_30,(0,1,0):C.R2GC_147_27})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.u__tilde__, P.uv, P.p1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_171_46})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.uv, P.p2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_172_47})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.uv__tilde__, P.uv, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.uv__tilde__, P.uv, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_129_18})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_110_17})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_110_17})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_110_17})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_26,(0,1,0):C.R2GC_129_18})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_145_26,(0,1,0):C.R2GC_129_18})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_145_26,(0,1,0):C.R2GC_129_18})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_107_14})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_108_15})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_130_19})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_21,(0,1,0):C.R2GC_137_22})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_136_21,(0,1,0):C.R2GC_137_22})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_136_21,(0,1,0):C.R2GC_137_22})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_109_16})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_109_16})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_143_25,(0,2,0):C.R2GC_143_25,(0,1,0):C.R2GC_109_16,(0,3,0):C.R2GC_109_16})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_109_16})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_109_16})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_135_20,(0,2,0):C.R2GC_135_20,(0,1,0):C.R2GC_109_16,(0,3,0):C.R2GC_109_16})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.uv__tilde__, P.uv ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_165_45,(0,2,0):C.R2GC_165_45,(0,1,0):C.R2GC_109_16,(0,3,0):C.R2GC_109_16})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.uv] ], [ [P.g] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,2):C.R2GC_154_35,(0,1,0):C.R2GC_80_61,(0,1,3):C.R2GC_80_62,(0,1,4):C.R2GC_80_63,(0,2,1):C.R2GC_153_33,(0,2,2):C.R2GC_153_34})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_75_51,(0,0,1):C.R2GC_75_52})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_88_74,(0,1,0):C.R2GC_88_74,(0,2,0):C.R2GC_88_74})

V_50 = CTVertex(name = 'V_50',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_81_64,(0,0,1):C.R2GC_81_65,(0,0,2):C.R2GC_81_66,(0,1,0):C.R2GC_81_64,(0,1,1):C.R2GC_81_65,(0,1,2):C.R2GC_81_66,(0,2,0):C.R2GC_81_64,(0,2,1):C.R2GC_81_65,(0,2,2):C.R2GC_81_66})

V_51 = CTVertex(name = 'V_51',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_83_70,(0,0,1):C.R2GC_83_71,(0,0,2):C.R2GC_83_72,(0,1,0):C.R2GC_83_70,(0,1,1):C.R2GC_83_71,(0,1,2):C.R2GC_83_72,(0,2,0):C.R2GC_83_70,(0,2,1):C.R2GC_83_71,(0,2,2):C.R2GC_83_72})

V_52 = CTVertex(name = 'V_52',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u], [P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_78_57,(0,0,1):C.R2GC_78_58,(0,1,0):C.R2GC_78_57,(0,1,1):C.R2GC_78_58,(0,2,0):C.R2GC_78_57,(0,2,1):C.R2GC_78_58})

V_53 = CTVertex(name = 'V_53',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ], [ [P.uv] ] ],
                couplings = {(1,0,0):C.R2GC_77_55,(1,0,1):C.R2GC_77_56,(0,1,0):C.R2GC_82_67,(0,1,1):C.R2GC_82_68,(0,1,2):C.R2GC_82_69,(0,2,0):C.R2GC_82_67,(0,2,1):C.R2GC_82_68,(0,2,2):C.R2GC_82_69,(0,3,0):C.R2GC_82_67,(0,3,1):C.R2GC_82_68,(0,3,2):C.R2GC_82_69})

V_54 = CTVertex(name = 'V_54',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u], [P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_79_59,(0,0,1):C.R2GC_79_60,(0,1,0):C.R2GC_79_59,(0,1,1):C.R2GC_79_60,(0,2,0):C.R2GC_79_59,(0,2,1):C.R2GC_79_60})

V_55 = CTVertex(name = 'V_55',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_76_53,(0,0,1):C.R2GC_76_54})

V_56 = CTVertex(name = 'V_56',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_76_53,(0,0,1):C.R2GC_76_54})

V_57 = CTVertex(name = 'V_57',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_87_73})

V_58 = CTVertex(name = 'V_58',
                type = 'R2',
                particles = [ P.g, P.g, P.p1, P.p1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.u, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_173_48})

V_59 = CTVertex(name = 'V_59',
                type = 'R2',
                particles = [ P.g, P.g, P.p1, P.p2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.u, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_174_49})

V_60 = CTVertex(name = 'V_60',
                type = 'R2',
                particles = [ P.g, P.g, P.p2, P.p2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.u, P.uv] ] ],
                couplings = {(0,0,0):C.R2GC_175_50})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,1,0):C.UVGC_155_65,(0,1,1):C.UVGC_155_66,(0,1,4):C.UVGC_155_67,(0,1,5):C.UVGC_155_68,(0,2,2):C.UVGC_90_107,(0,0,3):C.UVGC_91_108})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5, L.VVVV9 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u], [P.uv] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(2,0,3):C.UVGC_101_4,(2,0,4):C.UVGC_101_3,(0,0,3):C.UVGC_101_4,(0,0,4):C.UVGC_101_3,(4,0,3):C.UVGC_100_1,(4,0,4):C.UVGC_100_2,(3,0,3):C.UVGC_100_1,(3,0,4):C.UVGC_100_2,(8,0,3):C.UVGC_101_3,(8,0,4):C.UVGC_101_4,(7,0,0):C.UVGC_160_88,(7,0,2):C.UVGC_160_89,(7,0,3):C.UVGC_160_90,(7,0,4):C.UVGC_160_91,(7,0,5):C.UVGC_160_92,(7,0,6):C.UVGC_160_93,(6,0,0):C.UVGC_160_88,(6,0,2):C.UVGC_160_89,(6,0,3):C.UVGC_161_94,(6,0,4):C.UVGC_161_95,(6,0,5):C.UVGC_160_92,(6,0,6):C.UVGC_160_93,(5,0,3):C.UVGC_100_1,(5,0,4):C.UVGC_100_2,(1,0,3):C.UVGC_100_1,(1,0,4):C.UVGC_100_2,(11,3,3):C.UVGC_104_7,(11,3,4):C.UVGC_104_8,(10,3,3):C.UVGC_104_7,(10,3,4):C.UVGC_104_8,(9,3,3):C.UVGC_103_5,(9,3,4):C.UVGC_103_6,(2,1,3):C.UVGC_101_4,(2,1,4):C.UVGC_101_3,(0,1,3):C.UVGC_101_4,(0,1,4):C.UVGC_101_3,(6,1,0):C.UVGC_157_75,(6,1,3):C.UVGC_157_76,(6,1,4):C.UVGC_157_77,(6,1,5):C.UVGC_157_78,(6,1,6):C.UVGC_157_79,(4,1,3):C.UVGC_100_1,(4,1,4):C.UVGC_100_2,(3,1,3):C.UVGC_100_1,(3,1,4):C.UVGC_100_2,(8,1,0):C.UVGC_159_82,(8,1,2):C.UVGC_159_83,(8,1,3):C.UVGC_159_84,(8,1,4):C.UVGC_159_85,(8,1,5):C.UVGC_159_86,(8,1,6):C.UVGC_159_87,(7,1,1):C.UVGC_105_9,(7,1,3):C.UVGC_106_11,(7,1,4):C.UVGC_106_12,(5,1,3):C.UVGC_100_1,(5,1,4):C.UVGC_100_2,(1,1,3):C.UVGC_100_1,(1,1,4):C.UVGC_100_2,(0,2,3):C.UVGC_101_4,(0,2,4):C.UVGC_101_3,(2,2,3):C.UVGC_101_4,(2,2,4):C.UVGC_101_3,(5,2,3):C.UVGC_100_1,(5,2,4):C.UVGC_100_2,(1,2,3):C.UVGC_100_1,(1,2,4):C.UVGC_100_2,(7,2,0):C.UVGC_157_75,(7,2,3):C.UVGC_158_80,(7,2,4):C.UVGC_158_81,(7,2,5):C.UVGC_157_78,(7,2,6):C.UVGC_157_79,(4,2,3):C.UVGC_100_1,(4,2,4):C.UVGC_100_2,(3,2,3):C.UVGC_100_1,(3,2,4):C.UVGC_100_2,(8,2,0):C.UVGC_156_69,(8,2,2):C.UVGC_156_70,(8,2,3):C.UVGC_156_71,(8,2,4):C.UVGC_156_72,(8,2,5):C.UVGC_156_73,(8,2,6):C.UVGC_156_74,(6,2,1):C.UVGC_105_9,(6,2,3):C.UVGC_105_10,(6,2,4):C.UVGC_103_5})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.uv__tilde__, P.uv, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_110_16,(0,1,0):C.UVGC_163_97})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.uv__tilde__, P.u, P.p2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.uv] ], [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_172_104,(0,0,2):C.UVGC_172_105,(0,0,1):C.UVGC_172_106})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.uv__tilde__, P.u, P.p1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.uv] ], [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_171_101,(0,0,2):C.UVGC_171_102,(0,0,1):C.UVGC_171_103})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_148_46,(0,0,2):C.UVGC_148_47,(0,0,1):C.UVGC_148_48,(0,1,0):C.UVGC_149_49,(0,1,2):C.UVGC_149_50,(0,1,1):C.UVGC_149_51})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_139_34})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_138_33})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_151_55})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_152_56})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_150_52,(0,0,2):C.UVGC_150_53,(0,0,1):C.UVGC_150_54,(0,1,0):C.UVGC_147_43,(0,1,2):C.UVGC_147_44,(0,1,1):C.UVGC_147_45})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.u__tilde__, P.uv, P.p1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.uv] ], [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_171_101,(0,0,2):C.UVGC_171_102,(0,0,1):C.UVGC_171_103})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.uv, P.p2 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS5 ],
                loop_particles = [ [ [P.g, P.u] ], [ [P.g, P.u, P.uv] ], [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_172_104,(0,0,2):C.UVGC_172_105,(0,0,1):C.UVGC_172_106})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.uv__tilde__, P.uv, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV4 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.uv] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,4):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,2):C.UVGC_111_19,(0,1,3):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,4):C.UVGC_164_98})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.uv__tilde__, P.uv, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.uv] ] ],
                couplings = {(0,0,0):C.UVGC_129_24,(0,1,0):C.UVGC_166_100,(0,2,0):C.UVGC_166_100})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_110_16,(0,1,0):C.UVGC_93_110,(0,2,0):C.UVGC_93_110})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_110_16,(0,1,0):C.UVGC_93_110,(0,2,0):C.UVGC_93_110})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_110_16,(0,1,0):C.UVGC_141_36,(0,2,0):C.UVGC_141_36})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,4):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,2):C.UVGC_111_19,(0,1,3):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,4):C.UVGC_111_23,(0,2,0):C.UVGC_111_17,(0,2,1):C.UVGC_111_18,(0,2,2):C.UVGC_111_19,(0,2,3):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,4):C.UVGC_111_23})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,2):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,3):C.UVGC_111_19,(0,1,4):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,2):C.UVGC_111_23,(0,2,0):C.UVGC_111_17,(0,2,1):C.UVGC_111_18,(0,2,3):C.UVGC_111_19,(0,2,4):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,2):C.UVGC_111_23})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,4):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,2):C.UVGC_111_19,(0,1,3):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,4):C.UVGC_142_37,(0,2,0):C.UVGC_111_17,(0,2,1):C.UVGC_111_18,(0,2,2):C.UVGC_111_19,(0,2,3):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,4):C.UVGC_142_37})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_130_25,(0,0,1):C.UVGC_130_26})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_130_25,(0,0,1):C.UVGC_130_26})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_144_39,(0,0,2):C.UVGC_144_40,(0,0,1):C.UVGC_130_26})

V_85 = CTVertex(name = 'V_85',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_145_41,(0,1,0):C.UVGC_146_42})

V_86 = CTVertex(name = 'V_86',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_107_13,(0,1,0):C.UVGC_95_111,(0,2,0):C.UVGC_95_111})

V_87 = CTVertex(name = 'V_87',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_107_13,(0,1,0):C.UVGC_95_111,(0,2,0):C.UVGC_95_111})

V_88 = CTVertex(name = 'V_88',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_107_13,(0,1,0):C.UVGC_133_28,(0,2,0):C.UVGC_133_28})

V_89 = CTVertex(name = 'V_89',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,2):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,3):C.UVGC_111_19,(0,1,4):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,2):C.UVGC_111_23,(0,2,0):C.UVGC_111_17,(0,2,1):C.UVGC_111_18,(0,2,3):C.UVGC_111_19,(0,2,4):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,2):C.UVGC_111_23})

V_90 = CTVertex(name = 'V_90',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,4):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,1):C.UVGC_111_18,(0,1,2):C.UVGC_111_19,(0,1,3):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,4):C.UVGC_111_23,(0,2,0):C.UVGC_111_17,(0,2,1):C.UVGC_111_18,(0,2,2):C.UVGC_111_19,(0,2,3):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,4):C.UVGC_111_23})

V_91 = CTVertex(name = 'V_91',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                couplings = {(0,0,1):C.UVGC_108_14,(0,1,0):C.UVGC_111_17,(0,1,2):C.UVGC_111_18,(0,1,3):C.UVGC_111_19,(0,1,4):C.UVGC_111_20,(0,1,5):C.UVGC_111_21,(0,1,6):C.UVGC_111_22,(0,1,1):C.UVGC_134_29,(0,2,0):C.UVGC_111_17,(0,2,2):C.UVGC_111_18,(0,2,3):C.UVGC_111_19,(0,2,4):C.UVGC_111_20,(0,2,5):C.UVGC_111_21,(0,2,6):C.UVGC_111_22,(0,2,1):C.UVGC_134_29})

V_92 = CTVertex(name = 'V_92',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_130_25,(0,0,1):C.UVGC_130_26})

V_93 = CTVertex(name = 'V_93',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_130_25,(0,0,1):C.UVGC_130_26})

V_94 = CTVertex(name = 'V_94',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_144_39,(0,0,2):C.UVGC_144_40,(0,0,1):C.UVGC_130_26})

V_95 = CTVertex(name = 'V_95',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_136_31,(0,1,0):C.UVGC_137_32})

V_96 = CTVertex(name = 'V_96',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_109_15,(0,1,0):C.UVGC_92_109,(0,2,0):C.UVGC_92_109})

V_97 = CTVertex(name = 'V_97',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_109_15,(0,1,0):C.UVGC_92_109,(0,2,0):C.UVGC_92_109})

V_98 = CTVertex(name = 'V_98',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_143_38,(0,2,0):C.UVGC_143_38,(0,1,0):C.UVGC_140_35,(0,3,0):C.UVGC_140_35})

V_99 = CTVertex(name = 'V_99',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_109_15,(0,1,0):C.UVGC_92_109,(0,2,0):C.UVGC_92_109})

V_100 = CTVertex(name = 'V_100',
                 type = 'UV',
                 particles = [ P.s__tilde__, P.s ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF1, L.FF3, L.FF5 ],
                 loop_particles = [ [ [P.g, P.s] ] ],
                 couplings = {(0,0,0):C.UVGC_109_15,(0,1,0):C.UVGC_92_109,(0,2,0):C.UVGC_92_109})

V_101 = CTVertex(name = 'V_101',
                 type = 'UV',
                 particles = [ P.b__tilde__, P.b ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.b, P.g] ] ],
                 couplings = {(0,0,0):C.UVGC_135_30,(0,2,0):C.UVGC_135_30,(0,1,0):C.UVGC_132_27,(0,3,0):C.UVGC_132_27})

V_102 = CTVertex(name = 'V_102',
                 type = 'UV',
                 particles = [ P.uv__tilde__, P.uv ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                 loop_particles = [ [ [P.g, P.uv] ] ],
                 couplings = {(0,0,0):C.UVGC_165_99,(0,2,0):C.UVGC_165_99,(0,1,0):C.UVGC_162_96,(0,3,0):C.UVGC_162_96})

V_103 = CTVertex(name = 'V_103',
                 type = 'UV',
                 particles = [ P.g, P.g ],
                 color = [ 'Identity(1,2)' ],
                 lorentz = [ L.VV1, L.VV3 ],
                 loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ], [ [P.uv] ] ],
                 couplings = {(0,0,0):C.UVGC_154_60,(0,0,1):C.UVGC_154_61,(0,0,2):C.UVGC_154_62,(0,0,3):C.UVGC_154_63,(0,0,4):C.UVGC_154_64,(0,1,0):C.UVGC_153_57,(0,1,3):C.UVGC_153_58,(0,1,4):C.UVGC_153_59})

