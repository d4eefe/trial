import htmap as ht

def job(x):
    import torch

    return {"x": x, "version": torch.__version__, "cuda": torch.cuda.is_available()}


if __name__ == "__main__":
    ht.settings["DELIVERY_METHOD"] = "docker"
    ht.settings["MAP_OPTIONS.REQUEST_MEMORY"] = "250MB"
    ht.settings["DOCKER.IMAGE"] = "at3cat3st4age/dfvaea431a"

    future = ht.map(job, range(4), tag="test-1")
    print(future)
    #  results = list(future)
    #  print(results)


    #  for result in future:
    #  print(result)

    #  options = {
    #  "request_cpus": "1",
    #  "request_gpus": "1",
    #  "Requirements": "(Target.CUDADriverVersion >= 10.1)",
    #  }
    #  future = map(job, range(10)
    #  ht.status()
    #  ht.load("test-2")
