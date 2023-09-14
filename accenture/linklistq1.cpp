#include<iostream>
using namespace std;
struct Node{
    int data;
    Node *next;
};
//print the linked list
void printList(Node *n){
    int count=0;
    while(n!=NULL){
        cout<<n->data<<endl;
        n=n->next;
        count++;
        
    }
    cout<<"the total no of element in linked list"<<count<<endl;
}
// Node *pushfront(Node *head,int ndata){
//     Node *newNode=new Node();
//     newNode->data=ndata;
//     newNode->next=head;
//     head=newNode;
//     return head;
// }
//insert a data at first node or at head of linked list
void pushfront(Node **head_ref,int ndata){
    Node *newNode=new Node();
    newNode->data=ndata;
    newNode->next=*head_ref;
    *head_ref=newNode;
}
void pushafter(Node *prevnode,int ndata)
{
    Node *newNode = new Node();
    newNode->data=ndata;
    newNode->next=prevnode->next;
    prevnode->next=newNode;
}
//
void pushlast(Node **head_ref,int ldata)
{
    Node *newNode=new Node();
    newNode->data=ldata;
    newNode->next=NULL;
    Node *last=*head_ref;
    if(*head_ref==NULL)
    {
        last = newNode;
        return;
    }
    while(last->next!=NULL)
    {
        last=last->next;
    }
    last->next = newNode;
    return;

}
//delete a node from link list
void deletenode(Node **head_ref,int key)
{
    Node *prevnode;
    Node *temp;
    temp=*head_ref;

    //if key is present in head 
    if(temp->data==key && temp!=NULL)
    {
        *head_ref=temp->next;
        free(temp);
    }
    //now traversing in linkedlist
    while(temp!=NULL && temp->data!=key)
    {
        prevnode=temp;
        temp=temp->next;
    }
    //if key is not found
    if(temp==NULL) return;

    //if key is found
    prevnode->next=temp->next;
    free(temp);
    
}
void printlist(Node *head)
{
    while(head!=NULL)
    {
        cout<<head->data;
        head = head->next;
    }
}
int main()
{
    Node *head=NULL; 
    pushfront(&head,5);
    pushfront(&head,7);
    pushfront(&head,-3);
    pushafter(head->next,21);
    pushlast(&head,20);

    printList(head);
    deletenode(&head,7);
    printList(head);
    printlist(head);
    return 0;
}