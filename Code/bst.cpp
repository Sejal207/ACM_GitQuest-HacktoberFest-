#include <iostream>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node(int data) {
        val = data;
        left = NULL;
        right = NULL;
    }
};

void insert(int val, Node* &root) {
    if (root == NULL) {
        root = new Node(val);
        return;
    }

    if (val > root->val) {
        insert(val, root->right);
    } else {
        insert(val, root->left);
    }
}

void preorder(Node* root) {
    if (root == NULL) {
        return;
    }
    cout << root->val << " ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(Node* root) {
    if (root == NULL) {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout << root->val << " ";
}

void inorder(Node* root) {
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

int main() {
    Node* root = NULL;
    insert(2, root);
    insert(1, root);
    insert(3, root);
    cout << "Inorder traversal: ";
    inorder(root);
    cout << endl;

    cout << "Preorder traversal: ";
    preorder(root);
    cout << endl;

    cout << "Postorder traversal: ";
    postorder(root);
    cout << endl;

    return 0;
}
