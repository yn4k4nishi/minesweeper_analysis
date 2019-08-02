# coding:utf-8
import numpy as np

from edge_mask import edge_mask
from edge_mask import edge
from trans_mat import trans_mat

def debug_8x8(mat):
    tmp = 1
    for i in mat:
        tmp %= 8
        # print("{:3.2f}".format(i), end = '\t')
        print("{}".format(i), end = '\t')
        if tmp == 0:
            print()
        tmp += 1
    print()

def thin_mat(mat, save_indexs, num):
    rm_index = []
    for i in range(64):
        if i in edge:
            continue
        rm_index.append(i)
    # print(rm_index)
    if num == 2:
        ret = np.delete(mat, rm_index, axis = 0)
        ret = np.delete(ret, rm_index, axis = 1)
    if num == 1:
        ret = np.delete(mat, rm_index, axis = 0)
    return ret



if __name__ == "__main__":
    ## for 8x8
    board = np.array([[
        0,0,0,0,0,1,0,0,
        0,1,1,1,0,1,2,0,
        0,2,0,2,0,0,2,0,
        1,3,0,3,1,0,2,0,
        0,0,0,0,1,0,1,0,
        0,0,0,0,2,1,1,0,
        0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0
        #,10 # bomb number
    ]])

    board = np.transpose(board)

    print("--- matrix size ---")
    print("baord size     : " ,np.shape(board))
    print("edge mask size : ", np.shape(edge_mask))
    print("trans mat size : " ,np.shape(trans_mat))
    print()

    a = thin_mat(trans_mat,edge,2)
    b = thin_mat(board,edge,1)
    print("a shape : ",np.shape(a))
    print("b shape : ",np.shape(b))
    print(np.linalg.matrix_rank(a))
    print(np.linalg.matrix_rank(b))
    # print(b)

    ##################################################################################
    # A = np.matrix(trans_mat)
    # b = np.matrix(board)
    # alpha = 0
    # x = np.zeros((65,1))
    # m = A.T * (A*x-b)
    # t = -(np.tensordot(m,A.T*(A*x-b)))/(np.tensordot(m,A.T*A*m))
    # x = x + t*m

    # for i in range(10000):
    #     alpha = - (np.tensordot(m,A.T * A * A.T*(A*x-b)))/(np.tensordot(m, A.T*A*m))
    #     m = A.T * (A*x-b) + alpha*m
    #     t = -(np.tensordot(m,A.T*(A*x-b)))/(np.tensordot(m,A.T*A*m))
    #     x = x + t*m

    ##################################################################################
    # import scipy.linalg as linalg
    # LU = linalg.lu_factor(a)
    # x = linalg.lu_solve(LU, b)

    ##################################################################################
    # x = np.linalg.solve(a, board)
    x = np.linalg.solve(a, b)

    ##################################################################################
    # pinv_trans_mat = np.linalg.pinv(trans_mat)
    # x = np.dot(trans_mat,board)

    ##################################################################################
    print(x)
    print(np.shape(x))
    # debug_8x8(np.transpose(x))
