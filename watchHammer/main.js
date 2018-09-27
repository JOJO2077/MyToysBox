function node(code, parents, str) {
    this.path = str;
    this.code = code;
    this.parents = parents;
}

node.prototype.check = function (code) {
    var n = this;
    while (n != null && n.code != code) {
        n = n.parents;
    }
    return n == null;
}

function main(array) {
    while (true) {
        var thisnode = array.shift();
        var num = thisnode.code;
        var str = thisnode.path;
        if (num == 0b111111111 || str.length > 514) {
            console.log("DONE:", str);
            break;
        }
        for (var i = 0; i < 9; i++) {
            var c = next(num, i);
            if (thisnode.check(c)) {
                var s = str + i;
                var n = new node(c, thisnode, s);
                array.push(n);
            }

        }
    }
}

function next(num, pos) {
    if (pos + 3 < 9) {
        var t = 0b1;
        t = t << (pos + 3);
        num = num ^ t;
    }
    if (pos - 3 >= 0) {
        var t = 0b1;
        t = t << (pos - 3);
        num = num ^ t;
    }
    if (pos % 3 != 2) {
        var t = 0b1;
        t = t << (pos + 1);
        num = num ^ t;
    }
    if (pos % 3 != 0) {
        var t = 0b1;
        t = t << (pos - 1);
        num = num ^ t;
    }
    var t = 0b1;
    t = t << pos;
    num = num ^ t;
    return num;
}

var queue=new Array()
var arr = 0b000001100
//          876543210
var root = new node(arr, null,"::");
queue.push(root);
var start=Date.now()
main(queue);
console.log(Date.now()-start,"ms");