/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    cnt = init
    return { 
        increment(){
            cnt = cnt + 1 
            return cnt
        },
        decrement(){
            cnt = cnt - 1 
            return cnt
        },
        reset(){
            cnt = init 
            return cnt
        }
    }
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */