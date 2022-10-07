import copy
from random import randint

class Node:
    def __init__(self, depth, parent, state, turn):
        
        self.turn=turn
        self.depth=depth
        self.parent=parent
        self.state=state
        self.children=[]

        self.strength=self.getstrength()


        self.createChildren()

    def createChildren(self):
        if self.depth>=0 and self.turn>0: 
            ''' turn = 1 this code executes when comps turn (left tuple attacking right tuple)'''
            if self.state[1][0]!=0 and self.state[0][0] !=0:
                ll = self.state[1][0] + self.state[0][0]
                if ll>=5:
                    ll=ll-5
                s1 = copy.deepcopy(self.state)
                s1[1][0]=ll
                self.children.append(Node(self.depth-1, self, s1, -self.turn))

            if self.state[1][1]!=0 and self.state[0][0] !=0:
                lr = self.state[1][1] + self.state[0][0]
                if lr>=5:
                    lr=lr-5
                s2 = copy.deepcopy(self.state)
                s2[1][1]=lr
                self.children.append(Node(self.depth-1, self, s2, -self.turn))

            if self.state[1][0]!=0 and self.state[0][1] !=0:
                rl = self.state[1][0] + self.state[0][1]
                if rl>=5:
                    rl=rl-5
                s3 = copy.deepcopy(self.state)
                s3[1][0] = rl
                self.children.append(Node(self.depth-1, self, s3, -self.turn))

            if self.state[1][1]!=0 and self.state[0][1] !=0:
                rr = self.state[1][1] + self.state[0][1]
                if rr>=5:
                    rr=rr-5
                s4 = copy.deepcopy(self.state)
                s4[1][1] = rr
                self.children.append(Node(self.depth-1, self, s4, -self.turn))

            if self.state[0][1]%2==0 and self.state[0][0]==0:
                k5=copy.deepcopy(self.state)
                k5[0][0] = self.state[0][1]//2
                k5[0][1] = self.state[0][1]//2
                self.children.append(Node(self.depth-1, self, k5, -self.turn))

            elif self.state[0][0]%2==0 and self.state[0][1]==0:
                k5=copy.deepcopy(self.state)
                k5[0][0] = self.state[0][0]//2
                k5[0][1] = self.state[0][0]//2
                self.children.append(Node(self.depth-1, self, k5, -self.turn))

        elif self.depth>=0 and self.turn<0: 
            ''' turn = -1 this code executes when players turn (right tuple attacking left tuple)'''
            if self.state[1][0]!=0 and self.state[0][0] !=0:
                ll = self.state[1][0] + self.state[0][0]
                if ll>=5:
                    ll=ll-5
                s1 = copy.deepcopy(self.state)
                s1[0][0]=ll
                self.children.append(Node(self.depth-1, self, s1, -self.turn))

            if self.state[1][1]!=0 and self.state[0][0] !=0:
                lr = self.state[1][1] + self.state[0][0]
                if lr>=5:
                    lr=lr-5
                s2 = copy.deepcopy(self.state)
                s2[0][0]=lr
                self.children.append(Node(self.depth-1, self, s2, -self.turn))

            if self.state[1][0]!=0 and self.state[0][1] !=0:
                rl = self.state[1][0] + self.state[0][1]
                if rl>=5:
                    rl=rl-5
                s3 = copy.deepcopy(self.state)
                s3[0][1] = rl
                self.children.append(Node(self.depth-1, self, s3, -self.turn))

            if self.state[1][1]!=0 and self.state[0][1] !=0:
                rr = self.state[1][1] + self.state[0][1]
                if rr>=5:
                    rr=rr-5
                s4 = copy.deepcopy(self.state)
                s4[0][1] = rr
                self.children.append(Node(self.depth-1, self, s4, -self.turn))

            if self.state[1][1]%2==0 and self.state[1][0]==0:
                k5=copy.deepcopy(self.state)
                k5[1][0] = self.state[1][1]//2
                k5[1][1] = self.state[1][1]//2
                self.children.append(Node(self.depth-1, self, k5, -self.turn))

            elif self.state[1][0]%2==0 and self.state[1][1]==0:
                k5=copy.deepcopy(self.state)
                k5[1][0] = self.state[1][0]//2
                k5[1][1] = self.state[1][0]//2
                self.children.append(Node(self.depth-1, self, k5, -self.turn))


    def getstrength(self):
        if self.state[1][1]==0 and self.state[1][0]==0:
            '''players tuple is all zeroes, comp wins'''
            return 1000
        elif self.state[0][1]==0 and self.state[0][0]==0:
            '''comps tuple is all zeroes, player wins'''
            return -1000
        else:
            return 0



def winCheck(state):
    if state[1][1]==0 and state[1][0]==0:
        win=1
        print(currentState[0], '\n', currentState[1], "comp wins!")
    elif state[0][1]==0 and state[0][0]==0:
        win=-1
        print('\n', currentState[0], '\n', currentState[1], "you win!")
    else:
        win=0
    return win

def miniMax(node, mDepth, turn):
    if(mDepth==0) or (abs(node.strength)==1000):
        return node.strength
        print('\n',node.state, node.strength, '\n')
    goal = 1000 * -turn

    for child in node.children:
        val = miniMax(child, mDepth-1, -turn)
        if abs(1000*turn-val) < abs(1000*turn-goal):
            goal=val

    return goal


def make_move(move, state):
    #originally intended to be utilized in tree generation as well, but as is
    #just handles the human player's turn
    if move=="pass":
        return state
    letter_to_array = {
        'l' : 0,
        'r' : 1
    }

    attack = {
        'l': state[1][0],
        'r': state[1][1]
    }
    defend = {
        'l': state[0][0],
        'r': state[0][1]
    }

    def _valid_split():
        if min(attack.values()) == 0 and sum(attack.values()) % 2 == 0:
            return True

    def _valid_move():
        if move == 'spl':
            return True
        if _get_attack() == 0:
            return False
        if (move[0] == 'l' or move[0] == 'r') and (move[1] == 'l' or move[1] == 'r'):
            return True

    def _split():
        if _valid_split():
            split = sum(attack.values()) // len(attack)
            attack['l'], attack['r'] = split, split

    def _get_attack():
        return attack[move[0]]

    def _get_defense():
        return defend[move[1]]

    def _apply_attack():
        result = _get_attack() + _get_defense()
        if result >= 5:
            result %= 5
        defend[move[1]] = result

    if _valid_move():
        if move == 'spl':
            _split()
        else:
            _apply_attack()

        state = [[defend['l'], defend['r']], [attack['l'], attack['r']]]
        return state

def aiMove(currentState):
    node = Node(9, None, currentState, -turn)

    bestChoice = []
    bestStrength = 0
    superChoice = -1
    for i in range(len(node.children)):
        child = node.children[i]
        val = miniMax(child,8,turn)
        if val >= bestStrength:
            bestStrength = val
            bestChoice.append(i)
            tVal=miniMax(child,3,turn)
            if tVal>=1000:
                superChoice=i
        
    if len(bestChoice)==0:
        bestChoice.append(0)
    i = randint(0,len(bestChoice)-1)
    if superChoice!=-1:
        i=superChoice
    t = bestChoice[i]
    return node.children[t].state


if __name__ == "__main__":
    currentState = [[1,1],[1,1]]
    turn = -1
    print('indicate move with ll lr rl rr')
    while winCheck(currentState) == 0:
        print(currentState[0], '\n', currentState[1])
        move = input('enter:')

        if not move in ('rr' , 'll' , 'rl' , 'lr' , 'spl' , 'pass'):
            print('Invalid move.')
            continue 
        
        attempted_state = make_move(move, currentState)
        if attempted_state != currentState:
            currentState = attempted_state
        else:
            print('Invalid move.')
            continue
        print(currentState[0], '\n', currentState[1])
        print('Computer\'s turn...')
        
        if winCheck(currentState) == 0:
            currentState = aiMove(currentState)
