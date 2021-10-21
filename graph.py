class Vertex:
    def __init__(self, id, prop):
        self.id = id
        self.prop = prop

class Edge:
    def __init__(self, srcid, dstid, weight):
        self.srcid = srcid
        self.dstid = dstid
        self.weight = weight

# BFS Custom Computation Specification
def Process_Edge(weight, src_prop, dst_prop):
    return src_prop

def Reduce(temp, res, itercount):
    return min(temp, itercount)

def Apply(vprop, temp, vconst):
    return temp 

def Run(Vertices, Edges, EdgeIDTable, VProperty, VTempProperty, VConst,
        ActiveVertex, ActiveVertexCount, IterCount):

    # Base Graph Processing Model
    for it in range(1, IterCount):
        # Processing Phase
        for i in range(0, ActiveVertexCount):
            src = ActiveVertex[i]
            eid = EdgeIDTable[src.id]
            e = Edges[eid]
            while e.srcid == src.id: 
                # dst.prop = VProperty[e.dstid]
                #print("Processing Edge: " + str(e.srcid) + " to " + str(e.dstid))
                res = Process_Edge(e.weight, VProperty[e.srcid], VProperty[e.dstid])
                temp = VTempProperty[e.dstid]
                temp = Reduce(temp, res, it)
                #print("Setting VTempProperty for edge " + str(e.dstid) + " to " + str(temp))
                VTempProperty[e.dstid] = temp
                eid = (eid + 1) % len(Edges)
                e = Edges[eid]

        # Reset ActiveVertex and ActiveVertexCount
        ActiveVertex = []
        ActiveVertexCount = 0

        # Apply Phase
        for i in range(0, len(Vertices)):
            vprop = VProperty[i]
            temp = VTempProperty[i]
            vconst = VConst[i]
            temp = Apply(vprop, temp, vconst)
            #print("Setting VProperty[" + str(i) + "]" + " to " + str(temp))
            VProperty[i] = temp
            if temp != vprop:
                #print("Adding vertex " + str(i) + " to ActiveVertex")
                v = Vertex(i, temp)
                ActiveVertex.append(v)
                ActiveVertexCount += 1
    print(VProperty)
    return VProperty
