# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pprint import pprint

from kubernetes import client, config


def main():
    """
    Update image of container1 in deployment deploy1:
    """
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    api_instance = client.AppsV1beta1Api()

    body = {
        "spec": {
            "template": {
                "spec": {
                    "containers": [
                        {
                            "name": "container1",
                            "image": "gcr.io/xxx/image:tag"
                        }
                    ]
                }
            }
        }
    }

    api_response = api_instance.patch_namespaced_deployment(
        'deploy1', 'default', body, pretty=True)

    pprint(api_response)


if __name__ == '__main__':
    main()
