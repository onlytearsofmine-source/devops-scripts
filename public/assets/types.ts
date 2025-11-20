export enum Environment {
  LOCAL = 'local',
  STAGING = 'staging',
  PRODUCTION = 'production',
}

export enum KubernetesClusterType {
  GKE = 'gke',
  AKS = 'aks',
  EKS = 'eks',
}

export enum GitOperation {
  PULL = 'pull',
  PUSH = 'push',
  MERGE = 'merge',
  REBASE = 'rebase',
}

export enum DockerImageAction {
  BUILD = 'build',
  PULL = 'pull',
  PUSH = 'push',
}

export enum TerraformOperation {
  PLAN = 'plan',
  APPLY = 'apply',
  DESTROY = 'destroy',
}

export enum TerraformBackendType {
  LOCAL = 'local',
  REMOTE = 'remote',
}

export enum HelmOperation {
  INSTALL = 'install',
  UPGRADE = 'upgrade',
  UNINSTALL = 'uninstall',
}

export enum KustomizeOperation {
  APPLY = 'apply',
  RESET = 'reset',
}

export enum GitProvider {
  GITHUB = 'github',
  BITBUCKET = 'bitbucket',
}